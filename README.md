# LogiNetwork
Login to IIITDM College Network

## Installation
- ### Linux
  ```
  bash <(curl -s https://raw.githubusercontent.com/abhishekmj303/LogiNetwork/master/linux/install.sh)
  ```
- ### Windows
  - [Python 3](https://www.python.org/downloads): Install from Microsoft Store
  - [msedgedriver.exe](https://msedgedriver.azureedge.net/101.0.1210.47/edgedriver_win64.zip) to be present in PATH
  - Download and extract the source code
  - To install required packages run inside the source directory:
    ```
    pip install -r requirements.txt
    ```

## Usage
Most efficient way to use the script is to run it from the shortcut keys.
- ### Linux:
  Default Hotkey is "Shift+Alt+i". To change the hotkey,
  1. Edit `/opt/LogiNetwork/hotkey.py`
  2. Restart service: ```systemctl --user restart loginet.service```
- ### Windows: 
  1. Create Shortcut file (.lnk) of the [Python file](loginet.py)
  2. Right-click the shortcut and set keyboard shortcut in the properties.