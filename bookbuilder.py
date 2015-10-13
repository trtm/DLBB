#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           : bookbuilder.py
# description     : :book: :hammer: Book Builder
# email           : dtrtrtm@gmail.com
# author          : https://github.com/trtm
# date            : 2015 10 12
# version         : 0.1

from __future__ import print_function
import os
import urllib2
import argparse
import subprocess
from time import sleep
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) \
    AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }

