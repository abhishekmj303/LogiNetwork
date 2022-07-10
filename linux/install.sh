#!/bin/bash

echo "LogiNetwork:"
echo "    Completely automate the College Wifi/LAN"
echo "    https//github.com/abhishekmj303/LogiNetwork"
echo

uname=$USER

if ! (nc -zw1 8.8.8.8 443); then
    echo "Please connect to the internet"
    exit 1
fi

ubuntu()
{
    sudo apt update
    if [[ $GIT -ne 0 ]]; then
        sudo apt install -y git
    fi
    if [[ $PIP -ne 0 ]]; then
        sudo apt install -y python3-pip
    fi
    if [[ $NOTIFY -ne 0 ]]; then
        sudo apt install -y libnotify-bin
    fi
    if [[ $GECKO -ne 0 ]]; then
        sudo apt install -y firefox-geckodriver
    fi
}

arch()
{
    read -p "Do you want to update system? [y/n] " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sudo pacman -Syu --noconfirm
    fi
    if [[ $GIT -ne 0 ]]; then
        sudo pacman -S --noconfirm git
    fi
    if [[ $PIP -ne 0 ]]; then
        sudo pacman -S --noconfirm python-pip
    fi
    if [[ $NOTIFY -ne 0 ]]; then
        sudo pacman -S --noconfirm libnotify
    fi
    if [[ $GECKO -ne 0 ]]; then
        sudo pacman -S --noconfirm geckodriver
    fi
}

git --version >/dev/null 2>&1
GIT=$?
pip3 -V >/dev/null 2>&1
PIP=$?
notify-send -v >/dev/null 2>&1
NOTIFY=$?
geckodriver -V >/dev/null 2>&1
GECKO=$?

set -e
if [[ $GIT -ne 0 || $PIP -ne 0 || $NOTIFY -ne 0 || $GECKO -ne 0 ]]; then
    echo "Installing Dependencies..."
    echo

    PS3="Please select the number for your OS / distro: "
    select _ in \
        "Ubuntu/Debian based" \
        "Arch Linux based"
    do
        case $REPLY in
        1) ubuntu
        break ;;
        2) arch
        break ;;
        *) echo "Invalid option"
        break ;;
        esac
    done
fi

sudo rm -rf /tmp/loginetwork
echo "Downloading LogiNetwork..."
git clone -q https://github.com/abhishekmj303/LogiNetwork.git /tmp/loginetwork
cd /tmp/loginetwork
echo "Installing python dependencies... (this may take a while)"
pip3 install -r requirements.txt >/dev/null

touch roll.txt
echo
echo "Enter your Login Credentials"
read -p "Username: " username
read -p "Password: " password
echo "${username},${password}" >roll.txt
echo

echo
echo "Installing the application..."
echo "  -Installation folder: /opt/LogiNetwork"
sudo mkdir -p /opt/LogiNetwork
sudo chown -R ${uname}:${uname} /opt/LogiNetwork
mv loginet.py /opt/LogiNetwork/
mv icon.ico /opt/LogiNetwork/
mv roll.txt /opt/LogiNetwork/
mv background.py /opt/LogiNetwork/
mv linux/uninstall.sh /opt/LogiNetwork/

echo "  -Creating a systemd service for user: ${uname}"
mkdir -p /home/${uname}/.config/systemd/user
mv linux/loginet.service /home/${uname}/.config/systemd/user/
systemctl --user enable loginet.service >/dev/null 2>&1
systemctl --user start loginet.service

echo "  -Installation complete"
echo
echo "College WiFi/LAN login is now automatically done"
echo "You can also explicitly use Ctrl+Alt+e to login (if not working properly)"