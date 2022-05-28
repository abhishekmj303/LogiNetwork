#!/bin/bash

set -e
uname=$USER

if ! (nc -zw1 8.8.8.8 443); then
    echo "Please connect to the internet"
    exit 1
fi

ubuntu()
{
    sudo apt update
    if [[ $GIT -ne 0 || $PIP -ne 0 ]]; then
        sudo apt install -y git python3-pip
    fi
    sudo apt install -y firefox-geckodriver libnotify-bin
}

arch()
{
    if [[ $GIT -ne 0 || $PIP -ne 0 ]]; then
        read -p "Do you want to update system? [y/n] " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            sudo pacman -Syu
        fi
        sudo pacman -S --noconfirm git python-pip
    fi
    sudo pacman -S --noconfirm geckodriver libnotify
}

git --version 2>&1 >/dev/null
GIT=$?
pip3 -V 2>&1 >/dev/null
PIP=$?

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

sudo rm -r /tmp/loginetwork
git clone https://github.com/abhishekmj303/LogiNetwork.git /tmp/loginetwork
cd /tmp/loginetwork
sudo pip3 install -r requirements.txt

touch roll.txt
echo
echo "Login Credentials"
read -p "Username: " username
read -p "Password: " password
echo "${username},${password}" >roll.txt
echo

sudo mkdir -p /opt/LogiNetwork
sudo chown -R ${uname}:${uname} /opt/LogiNetwork
mv loginet.py /opt/LogiNetwork/
mv hotkey.py /opt/LogiNetwork/
mv icon.ico /opt/LogiNetwork/
mv roll.txt /opt/LogiNetwork/
mv linux/uninstall.sh /opt/LogiNetwork/

mv linux/loginet.service /home/${uname}/.config/systemd/user/
systemctl --user ${uname} enable loginet.service
systemctl --user ${uname} start loginet.service

echo "Installation complete"
echo
echo ">>>> Use Shift+Ctrl+Alt+L to Login to College Network <<<<"