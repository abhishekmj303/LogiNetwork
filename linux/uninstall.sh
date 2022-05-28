#!/bin/bash

set -e

uname=$USER

systemctl --user $uname stop loginet.service
systemctl --user $uname disable loginet.service
rm /home/${uname}/.config/systemd/user/loginet.service

sudo rm -rf /opt/LogiNetwork