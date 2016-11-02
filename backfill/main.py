# # # # #
# Project: Backfill
# File: main.py
# Created by: Nathan Healea
# Description:
#   Main file for running Backfill program
# # # # #

# Import
import os
import sys
import requests
import json

#args, argv
def main():
    test()


    pass


def test():
    url = _url(prodDetection()) + '100'
    print 'URL: ' + url


    response = requests.get(url)
    data = json.loads(response.text)
    print 'JSON:\n'


def _url(path):
    return '' + path

def prodDetection():
    return ''


#*sys.argv
if __name__ == '__main__':
    main()