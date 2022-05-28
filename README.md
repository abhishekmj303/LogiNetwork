# LogiNetwork
Login to IIITDM College Network

## Installation
- ### Linux
  ```
  bash <(curl -s https://raw.githubusercontent.com/abhishekmj303/LogiNetwork/master/linux/install.sh)
  ```

## Requirements
- ### Windows
  - [Python 3](https://www.python.org/downloads)
  - [msedgedriver.exe](https://msedgedriver.azureedge.net/101.0.1210.47/edgedriver_win64.zip) to be present in PATH
  - Required packages:
    ```
    pip install -r requirements.txt
    ```
- ### Linux
  - pip, geckodriver and libnotify: (for Ubuntu)
    ```
    sudo apt install python3-pip firefox-geckodriver libnotify-bin
    ```
  - Required packages:
    ```
    pip3 install -r requirements.txt
    ```
## Usage
Most efficient way to use the script is to run it from the shortcut keys.
- Linux: Default Hotkey is "Shift+Ctrl+Alt+L"
- Windows: 
  1. Create Shortcut (.lnk) of the [Python file](loginet.py)
  2. Right-click the shortcut and set keyboard shortcut in the properties.