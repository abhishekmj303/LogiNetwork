# LogiNetwork
Login to IIITDM College Network

## Installation
- ### Linux
  ```
  bash <(curl -s https://raw.githubusercontent.com/abhishekmj303/LogiNetwork/master/linux/install.sh)
  ```
  **Note**: Install curl if not installed,
    - For Ubuntu: `sudo apt install curl`
    - For Arch: `sudo pacman -S curl`
- ### Windows
  - [Python 3](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5): Install from Microsoft Store
  - Run in PowerShell:
      ```
      iwr "https://raw.githubusercontent.com/abhishekmj303/LogiNetwork/master/win/install.py" -OutFile "install.py"; python .\install.py; rm install.py
      ```

## Usage
Most efficient way to use the script is to run it from the shortcut keys.

Default Hotkey is " **Ctrl+Alt+e** ". To change the hotkey,

- ### Linux:
  1. Edit `/opt/LogiNetwork/hotkey.py`
  2. Restart service: ```systemctl --user restart loginet.service```

  __Disable__: Stop and Disable service (`stop` and `disable` in place of `restart` above)

  __Uninstall__: `bash /opt/LogiNetwork/uninstall.sh`
- ### Windows: 
  1. Press " **Win+R** " and type " **shell:startup** "
  2. Edit `hotkey.pyw`
  3. Run `taskkill /IM pythonw.exe /F` and double click `hotkey.pyw`

  __Disable__: Kill task and Remove `hotkey.pyw` from startup folder
  
  __Uninstall__: Disable and Delete `LogiNetwork` in USER folder.