#! /bin/sh

printf "Closing web admin...\n"
pkill -f web_admin.py

printf "Clearing terminal...\n"
clear

printf "Exporting Python path...\n"
export PYTHONPATH=robbie/src/

printf "Lauching Web Admin...\n"
python3 robbie/src/programy/clients/web_admin/web_admin.py &

printf "Lauching Robbie...\n"
python3 robbie/src/programy/clients/console.py --config robbie/bots/robbie/config.yaml --cformat yaml --logging robbie/bots/robbie/logging.yaml --debug

