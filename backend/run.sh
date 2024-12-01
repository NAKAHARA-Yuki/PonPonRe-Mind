#!/bin/bash
/wait-for-it.sh db:3306 --timeout=30 --strict -- python ./run.py
