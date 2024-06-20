#!/usr/bin/env bash
#. venv/bin/activate
export UNIT_TESTING=TRUE
pytest || exit 1
