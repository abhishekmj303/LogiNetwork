#!/bin/bash

set -e

uname=$USER

systemctl --user stop loginet.service
systemctl --user disable loginet.service
rm /home/${uname}/.config/systemd/user/loginet.service

sudo rm -rf /opt/LogiNetwork