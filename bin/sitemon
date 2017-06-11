#!/usr/bin/python

from threading import Thread
import ConfigParser

from src.site_monitor import monitor

config = ConfigParser.ConfigParser()
config.read('config.ini')

hashes = config.get('Files', 'hash_file')
logs = config.get('Files', 'changes_file')

if __name__ == "__main__":

    webpages = config.get('WEBPAGES', 'webpages').split(',')

    for webpage in webpages:
        checker = Thread(target=monitor, args=([webpage,], hashes, logs))
        checker.start()
        checker.join()
