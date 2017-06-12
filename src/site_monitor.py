#!/usr/bin/python

from lib.site_monitor_lib import SiteMon

__author__ = "Tshaba Phomolo Benedict"

def monitor(webpage, hash_file, changes_file):
    """ Monitor the website, if there is a change log it to disk"""

    sm = SiteMon(hash_file, changes_file)

    changes = check_for_change(webpage, sm)
    if changes:
        sm.log(changes)
    print sm.show_report()

    sm.log("\nWebpage: "+webpage+" has not changed since last check.\n")

    return None

def check_for_change(webpage, sm):
    """ Gets the webpage and returns value of check_defacement"""

    page, err = sm.check_availability(webpage)
    if page is None:
        print page
        exit(-1)

    data = page.read()
    return sm.check_defacement(webpage, data)
