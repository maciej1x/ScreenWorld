#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import random
import string
import time

from selenium import webdriver, common
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class WebsiteScreenshot:
    def __init__(self, firefox_path,
                 geckodriver_path,
                 screenshots_path,
                 max_website_height=10000,
                 time_to_load=1):
        self.logger = logging.getLogger('WebsiteScreenshot')
        self.logger.setLevel(logging.INFO)
        self.firefox_path = firefox_path
        self.geckodriver_path = geckodriver_path
        self.logger.info("Starting browser")
        self.browser = self.start_browser(self.firefox_path, self.geckodriver_path)
        self.logger.info("Browser started")
        self.screenshots_path = screenshots_path
        self.max_website_height = max_website_height
        self.time_to_load = time_to_load


    @staticmethod
    def start_browser(firefox_path, geckodriver_path):

        # Create profile
        profile = webdriver.FirefoxProfile()

        # Set timeouts
        profile.set_preference("http.response.timeout", 60)
        profile.set_preference("dom.max_script_run_time", 20)

        # Disable cache and cookies
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        profile.set_preference("network.cookie.cookieBehavior", 2) # block all cookies by default

        # Run headless
        options = Options()
        options.headless = True
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        # Create browser
        browser = webdriver.Firefox(executable_path=geckodriver_path,
                                   firefox_binary=FirefoxBinary(firefox_path),
                                   firefox_profile=profile,
                                   options=options)
        browser.set_page_load_timeout(60) # Global timeout
        browser.set_script_timeout(20) # Scripts timeout
        browser.maximize_window()

        return browser

    def get_screenshot(self, url, scroll=True):
        self.logger.info(f'Loading page {url}')
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
        self.browser.get(url)
        time.sleep(self.time_to_load)
        self.logger.info('Page loaded')

        # Name for screenshot
        name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])+'.png'

        if scroll:
            # Get initial website width and height
            website_width = self.browser.execute_script('return document.body.parentNode.scrollWidth')
            website_height = self.browser.execute_script("return document.body.scrollHeight")

            # Scroll to the bottom of website
            while True:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                new_website_height = self.browser.execute_script("return document.body.scrollHeight")
                time.sleep(self.time_to_load) # Give second for all elements to load
                #  Break if website is longer than self.max_website_height or reached bottom of website
                if new_website_height == website_height or new_website_height > self.max_website_height:
                    break
                website_height = new_website_height

            # Sometimes website height/weight is readed as 0
            # in that case make screenshot without resizing window
            if website_height != 0 and website_width != 0:
                self.browser.set_window_size(website_width, website_height)
        self.browser.save_screenshot(os.path.join(self.screenshots_path, name))
        self.logger.info(f'Saved screenshot: {name}')
        self.browser.maximize_window()
        return os.path.join(self.screenshots_path, name)

    def __del__(self):
        self.browser.close()


