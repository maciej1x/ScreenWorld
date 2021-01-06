#!/bin/sh
#==================
# CHANGE DATA BELOW
LOGIN="sample@email"
PASSWORD="password1"
#==================

/usr/sbin/nordvpnd &
echo Initializing NordVPN
sleep 5
echo Logging to NordVPN...
nordvpn login --username=$LOGIN --password=$PASSWORD
echo Logged in
echo Starting app...
python3 app.py
