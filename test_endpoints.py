import pytest
import requests

url = 'http://127.0.0.1:5000'

def test_index_page():
    r = requests.get(url+'/')
    assert r.status_code == 200

def test_get_balance_in_transacations():
    r = requests.get(url+'/transactions/')
    data = r.json()

    assert r.status_code == 200
    assert data['balance'] == 0

def test_get_number_of_transacations():
    r = requests.get(url+'/transactions/')
    data = r.json()

    assert r.status_code == 200
    assert len(data['transactions']) != 0

def test_individual_transaction_fields():
    r = requests.get(url+'/transactions/')
    data = r.json()
    fields = list(data['transactions'])

    assert r.status_code == 200
    assert fields[0]['amount'] >= 0.00
    assert fields[0]['current_balance'] < 240
    assert 'jean' in fields[0]['description']
    assert 0 < fields[0]['id'] 
    assert 300 == fields[0]['inital_balance'] 
    assert "2019-01-12 09:00:00" == fields[0]['time']
    assert fields[0]['type'] != 'income'
