#!/bin/bash


cd /home/luisw/Documents/GIT/roomMonitor/
source .venv/bin/activate
cd Raspi/
python3 main.py &

exit