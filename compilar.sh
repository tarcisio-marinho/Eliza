#!/bin/bash
chmod +x esvaziar.sh tocar.sh teste.sh
sudo apt-get update
sudo apt-get install espeak
sudo apt-get install python-pip
sudo pip install requests
sudo python main.py
