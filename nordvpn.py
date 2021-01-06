#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import os

class NordVPN:
    def __init__(self):
        self.logger = logging.getLogger('NordVPN')
        self.logger.setLevel(logging.INFO)

    def login(self, username, password):
        """
        Login to NordVPN

        Parameters
        ----------
        username : str
            login.
        password : str
            password.

        Returns
        -------
        None.

        """
        output = os.popen(f'nordvpn login --username={username} --password={password}').read()
        self.logger.info(output)

    @staticmethod
    def clear_output(output):
        chars = '\|/- '
        text = ''
        for line in output.split('\n'):
            if len(line)>0 and line[0] not in chars:
                text += line + '\n'
        return text

    @staticmethod
    def countries():
        """
        Get list of available countries

        Returns
        -------
        countries : list
            list of countries.

        """
        countries = os.popen('nordvpn countries').readlines()[-1]
        countries = countries.replace('\n', '').split(', ')
        return countries

    @staticmethod
    def status():
        """
        Get status of connection

        Returns
        -------
        status : dict
            Status of connection and details about connection.

        """
        output = os.popen('nordvpn status').readlines()[6:]
        status = {}
        for field in output:
            status[field.split(': ')[0]] = field.split(': ')[1].replace('\n', '')
        for key in ['Status', 'Current server', 'Country', 'City', 'Your new IP', 'Current technology', 'Current protocol', 'Transfer', 'Uptime']:
            if key not in status.keys():
                status[key] = ''
        return status

    def connect(self, country=''):
        """
        Connect to VPN

        Parameters
        ----------
        country : str, optional
            Country you want be connected to. If left empty connects to closest
            The default is ''.

        Returns
        -------
        None.

        """
        output = os.popen(f'nordvpn c {country}').read()
        self.logger.info(self.clear_output(output))

    def disconnect(self):
        """
        Disconnect from VPN

        Returns
        -------
        None.

        """
        output = os.popen('nordvpn d').read()
        self.logger.info(self.clear_output(output))

