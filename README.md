# ScreenWorld
Get screenshot of given website for given country using VPN. Supports NordVPN.

## How to use
#### 1. Open (localhost:56777)[http://localhost:56777] in your browser.
#### 2. Enter URL and select a country
![Website before request](https://raw.githubusercontent.com/ulaszewskim/screenworld/main/_images/before.PNG)
#### 3. Click **Submit** and wait for screenshot
![Website after request](https://raw.githubusercontent.com/ulaszewskim/screenworld/main/_images/after.PNG)

## Requirement
#### 1. [NordVPN account](https://nordvpn.com/)
#### 2. NordVPN installed [Installation on Linux](https://support.nordvpn.com/Connectivity/Linux/1325531132/Installing-and-using-NordVPN-on-Debian-Ubuntu-Elementary-OS-and-Linux-Mint.htm)

## How to install
#### 1. Make sure you are logged to NordVPN
```
$ nordvpn account
Account Information:
Email Address: youremail@example.com
VPN Service: Active (Expires on Dec 10th, 2021)
```
#### 2. Download repo
```bash
git clone https://github.com/ulaszewskim/ScreenWorld.git
cd ScreenWorld
```
#### 3. (Optional) Create virtual environment
```bash
mkdir venv
python3 -m venv venv/
source ./venv/bin/activate
```
#### 4. Install libraries
```bash
pip3 install -r requirements.txt
```
#### 5. Download geckodriver
```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz
tar -zxvf geckodriver-v0.27.0-linux64.tar.gz
rm geckodriver-v0.27.0-linux64.tar.gz
```
#### 6. Download Firefox browser
```bash
wget https://download-installer.cdn.mozilla.net/pub/firefox/releases/81.0.1/linux-x86_64/pl/firefox-81.0.1.tar.bz2
tar -xvf firefox-81.0.1.tar.bz2
rm firefox-81.0.1.tar.bz2
```
**Warning!** If you chose to use different versions of geckodriver and Firefox [make sure they are compatible with each other](https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html)
#### 7. config.json
Change path to absolute if you want to run from different directory.

## How to run
```bash
python3 app.py
```

## TODO
[ ] Finish Docker container support