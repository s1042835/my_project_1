#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

host = config['http']['host']
port = int(config['http']['port'])

print(host)
print(port)