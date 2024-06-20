#!/usr/bin/env bash
python3.10 -m venv venv
. venv/bin/activate
pip3 install pip -i https://pypi.python.org/simple/
pip3 install -r requirements.txt
