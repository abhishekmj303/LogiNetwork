# LogiNetwork
Login to IIITDM College Network

## Requirements
- ### Windows
  - [Python 3](https://www.python.org/downloads)
  - [msedgedriver.exe](https://msedgedriver.azureedge.net/101.0.1210.47/edgedriver_win64.zip) to be present in PATH
  - Required packages:
    ```
    pip install -r requirements.txt
    ```
- ### Linux
  - pip3 and geckodriver (for Ubuntu):
    ```
    sudo apt-get install python3-pip firefox-geckodriver
    ```
  - Required packages:
    ```
    pip3 install -r requirements.txt
    ```
## Usage
Most efficient way to use the script is to run it from the shortcut keys.
- Linux: You can set custom keyboard shortcuts in your Settings App.
- Windows: 
  1. Create Shortcut (.lnk) of the [Python file](loginet.py)
  2. Right-click the shortcut and set keyboard shortcut in the properties.