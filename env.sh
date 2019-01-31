#!/usr/bin/env bash
pipenv shell
export FLASK_ENV=development FLASK_APP=expanses_manager.py
flask run