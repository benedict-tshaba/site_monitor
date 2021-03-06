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

    checkers = [Thread(target=monitor, args=(webpage, hashes, logs,)) for webpage in webpages]
    for checker in checkers:
        checker.start()
    for checker in checkers:
        checker.join()
