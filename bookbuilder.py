#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           : bookbuilder.py
# description     : :book: :hammer: Book Builder
# email           : dtrtrtm@gmail.com
# author          : https://github.com/trtm
# date            : 2015 10 12
# version         : 0.1
# licence         : WTFPL, http://www.wtfpl.net

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

#-------------------------------------------------------------------------------
# 0. Input

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--webpage', type=str , help='specify webpage')
parser.add_argument('-s', '--seconds', type=int, default=60, help='how many seconds to wait after printing')
args = parser.parse_args()

#
webpage = args.webpage
print( 'webpage:', webpage)

#
seconds = args.seconds
print( 'seconds:', seconds)

#
proc = subprocess.Popen(['echo $PWD', ''], stdout=subprocess.PIPE, shell=True)
out, err = proc.communicate()
PWD = str(out).replace('\n', '')
print( 'PWD:', PWD)

#-------------------------------------------------------------------------------
# 1. Use wget to get webpage content

os.system(u'wget -c -r -l1 %s' % webpage )

#-------------------------------------------------------------------------------
# 2. Create soup object

path = PWD + webpage.replace('http://', '/')
print( 'path:', path )

url = 'file://' + path + 'index.html'
print( 'url:', url )

#
req = urllib2.Request( url, None, headers )
response = urllib2.urlopen(req)
soup = BeautifulSoup(response, 'html.parser')

#-------------------------------------------------------------------------------
# 3. Print html files with Firefox

output_pdfs = []
for item in soup.find_all('a'):
    item = str(item)
    item = item.replace('<a href="', '')
    item = item.replace('</a>', '')
    link, name = item.split('">')
    link = link.replace('http://', '')

    if not 'version' in link and '.html' in link:
        orig = path + link
        output_pdf = orig.replace('.html', '.pdf')

        output_pdfs.append( output_pdf )

        if not os.path.isfile( output_pdf ):
            os.system(u'firefox -print %s -printmode pdf -printfile %s' % ( orig, output_pdf ) )
            sleep( seconds )
        else:
            print( 'already printed:', output_pdf )

#-------------------------------------------------------------------------------
# 4. Create argument of available single PDFs to merge

file_arg = ''
for f in output_pdfs:
    file_arg += f
    file_arg += ' '

#-------------------------------------------------------------------------------
# 5. Merge PDFs with pdftk

os.system(u'pdftk %s cat output ~/Desktop/DLB.pdf' % file_arg )



