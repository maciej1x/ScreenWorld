#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import os
import sys
import time

from flask import Flask, render_template, request
from flask_images import Images

from website_screenshot import WebsiteScreenshot
from nordvpn import NordVPN

app = Flask(__name__)
images = Images(app)

@app.route('/')
def home():
    if (status := nordvpn.status())['Status'] == 'Connected':
        vpn_status = status['Status']
        vpn_country = status['Country']
        vpn_ip = status['Your new IP']
    else:
        vpn_status = status['Status']
        vpn_country = ''
        vpn_ip = ''
    countries = nordvpn.countries()
    return render_template('form.html', **locals())


@app.route('/getscreenshot', methods=['POST'])
def getscreenshot():
    # Start timer
    start = time.time()
    # Inputs
    url = request.form['url']
    country = request.form['country']

    # Change VPN country if wanted is other than current
    if (current_country := nordvpn.status()['Country']) != country:
        nordvpn.connect(country=country)

    screenshot_name = webscr.get_screenshot(url, scroll=True)

    time_elapsed = int(time.time() - start)
    return render_template('result.html', **locals())


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout,
                        level=logging.INFO)
    logging.getLogger("selenium").setLevel(logging.INFO)
    logging.getLogger("urllib3").setLevel(logging.INFO)

    logger = logging.getLogger('ScreenWorld')
    logger.setLevel(logging.INFO)

    with open('config.json', 'r') as file:
        config = json.load(file)


    firefox_path = config['firefox_path']
    geckodriver_path = config['geckodriver_path']
    screenshots_path = 'static/' + config['screenshots_path']
    app.config['UPLOAD_FOLDER'] = screenshots_path
    if not os.path.exists('static'):
        os.mkdir('static')
    if not os.path.exists(screenshots_path):
        os.mkdir(screenshots_path)


    nordvpn = NordVPN()
    webscr = WebsiteScreenshot(firefox_path=firefox_path,
                                                 geckodriver_path=geckodriver_path,
                                                 screenshots_path=screenshots_path)

    app.run(port=56777, debug=False)
