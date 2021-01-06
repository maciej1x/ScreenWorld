#FROM ubuntu:18.04
FROM python:3.8-buster
# Install NordVPN

RUN apt update && apt upgrade -y && apt install -y wget unzip && \
    wget -O /tmp/nordrepo.deb https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb &&\
    apt-get update && apt-get install -y gnupg2 && \
    dpkg -i /tmp/nordrepo.deb && \
    apt update && apt upgrade -y && apt install -y nordvpn

# Copy files
COPY . /root/screenworld/

# Install pip libraries
WORKDIR /root/screenworld
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Download geckodriver and browser
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz
RUN tar -zxvf geckodriver-v0.27.0-linux64.tar.gz
RUN rm geckodriver-v0.27.0-linux64.tar.gz

RUN wget https://download-installer.cdn.mozilla.net/pub/firefox/releases/81.0.1/linux-x86_64/pl/firefox-81.0.1.tar.bz2
RUN tar -xvf firefox-81.0.1.tar.bz2
RUN rm firefox-81.0.1.tar.bz2

# Make startapp executable
RUN chmod +x ./startapp.sh

# Run
ENTRYPOINT ./startapp.sh
