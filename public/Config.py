#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
import os
import sys
from os import path


proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

class ReadConfig:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='UTF-8')

    def get_method(self):
        value = self.cf.get("DEVICES", 'method')
        return value

    def get_server_url(self):
        value = self.cf.get("DEVICES", "server")
        return value

    def get_server_token(self):
        value = self.cf.get("DEVICES", "token")
        return value

    def get_server_udid(self):
        value = self.cf.get("DEVICES", "udid")
        return value.split('|')

    def get_devices_ip(self):
        value = self.cf.get("DEVICES", "IP")
        return value.split('|')


    def get_dingding_token(self,project):
        value = self.cf.get("DINGDING TOKEN", project)
        return value

    def get_file_path(self,path):
        value = self.cf.get("FILE PATH", path)
        return value