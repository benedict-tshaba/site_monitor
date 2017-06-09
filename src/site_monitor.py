from threading import Lock, Thread
import urllib2
import hashlib
import pickle
import time

__version__ = "0.0.1"
__author__ = "Tshaba Phomolo Benedict"

file_lock = Lock()
hash_dict = {}
hash_file = "logs/hashes.txt"
changes_file = "logs/website_changes.log"

def log(msg):
    with file_lock:
        with open(changes_file, 'w') as f:
            f.write(msg)
    return None

def monitor(webpage=[]):
    """ Monitor the website, if there is a change log it to disk"""

    while True:
        changes = check_for_change(webpage)
        if changes:
            log(changes)
    return None

def check_for_change(webpage):
    """ Gets the webpage and returns value of check_defacement"""

    page = urllib2.urlopen(webpage)
    data = page.read()
    return check_defacement(webpage, data)

def check_defacement(pagename, data):
    """ Computes a checksum of the webpage and stores it, on subsequent calls
     it computes a checksum again and compares it with the one stored on disk if they dont match. 
     Then possibly the webpage has been defaced."""

    known_page_hash = {}
    try:
        f = file(hash_file, "rb")
        known_page_hash = pickle.load(f)
        f.close()
    except:
        pass

    try:
        if known_page_hash[pagename]:
            return None

    except KeyError:
        new_page_hash = md5(data)
        save_checksum(pagename, new_page_hash)         

    if md5(data) != known_page_hash[pagename]:
        msg = "Date: {0}".format(time.asctime())
        msg += "\nThe following "+webpage+" might have been maliciosly modified"
        msg += "\nPlease verify and restore from backup"
    
    return msg

def save_checksum(filename, filehash):
    """Computes checksum of file, stores it in a dictionary and saves it to disk"""
    
    hash_dict[filename] = filehash

    with open(hash_file, 'w') as f:
        #f.write(hashdict)
        pickle.dump(hash_dict, f)

    return None

def md5(data):
    """ returns a hash of the filename given in the argument"""

    file_hash = hashlib.sha1()
    file_hash.update(data)
    return file_hash.hexdigest()

if __name__ == "__main__":

    webpages = ['http://benedict.heliohost.org/index.html', 'http://benedict.heliohost.org/about.html'
    , 'http://benedict.heliohost.org/services.html', ]
    
    for webpage in webpages:
        checker = Thread(target=monitor, args=[webpage,])
        checker.start()
    checker.join()
