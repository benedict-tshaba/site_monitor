#!/usr/bin/python

import logging
from Queue import Queue
import pickle
from .site_monitor_lib import SiteMon

__author__ = "Tshaba Phomolo Benedict"

def monitor(webpage, hash_file, changes_file):
    """ Monitor the website, if there is a change log it to disk"""

    queue = Queue() #this solves the duplicates issue
    sm = SiteMon(hash_file, changes_file, queue)
    logging.basicConfig(filename=changes_file, level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p')

    changes = check_for_change(webpage, sm)
    if changes:
        logging.debug(changes)
        #sm.log(changes)
        print sm.show_report()
    
    else:
        logging.debug(" - File: "+webpage+" has not changed since last check")
        #sm.log("\nFile: "+webpage+" has not changed since last check.\n")

    while not queue.empty():
        with open(hash_file, 'w') as f:
            pickle.dump(queue.get(), f)

    return None

def check_for_change(webpage, sm):
    """ Gets the webpage and returns value of check_defacement"""

    page, err = sm.check_availability(webpage)
    if page is None:
        print err
        exit(-1)

    if webpage[-4:-1] == "htm" or webpage[-3:] == "php":
        data = page.read()
        return sm.check_defacement(webpage, data, 'txt')
    
    else:
        data = page.read()
        return sm.watch_files(webpage, data, 'bin')
