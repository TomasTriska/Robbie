#! /bin/sh

clear

export PYTHONPATH=robbie/src/

python3 robbie/src/programy/clients/console.py --config robbie/bots/robbie/config.yaml --cformat yaml --logging robbie/bots/robbie/logging.yaml --debug

