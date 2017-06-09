from threading import Lock, Thread
import urllib2
import pickle
import time

file_lock = Lock()
hashdict = {}
hashfile = "logs/hashes.txt"
changesf = "logs/website_changes.log"

def log(msg):
	with file_lock:
		open(changesf, 'w') as f:
			f.write(msg)
    return None

def monitor(webpage):
	""" Monitor the website, if there is a change log it to disk"""

	while True:
		changes = check_for_change(wepage)
		if changes not None:
			log(changes)
    return None

def check_for_change(webpage):
    page = urllib.urlopen(webpage)
    return check_defacement(webpage, page.read())

def check_defacement(pagename,data):
	""" Computes a checksum of the webpage and stores it, on subsequent calls it computes a checksum again and compares it with the one stored on disk if they dont match. Then Possibly the wepage has been defaced."""
    pagehash = picle.load(hashfile)
    if not pagehash[pagename]:
        thispagehash = md5(data)
        save_checksum(pagename, thispagehash)
    
    if md5(data) == pagehash[pagename]:
        return None

    else:
        msg = "Date: ".time.asctime()
        msg .= "\nThe following ".webpage." might have been maliciosly modified"
        msg .= "\nPlease verify and restore from backup"
    
	return msg

def save_checksum(filename, filehash):
    hashdict[filename] = filehash
    with open(hashfile) as f:
        #f.write(hashdict)
        pickle.dump(f,hashdict)
    return None

def md5(filename):
    """ returns a hash of the filename given in the argument"""
	filehash = hashlib.sha1()
	with open(filename, "rb") as f:
		for block in iter(lambda: f.read(4096), b""):
			filehash.update(block)
	return filehash.hexdigest()

if __name__ == "__main__":
	webpages = ['http://benedict.heliohost.org/index.html', 'http://benedict.heliohost.org/about.html', 'http://benedict.heliohost.org/', 'http://benedict.heliohost.org/services.html', ...]
	for webpage in webpages:
		checker = Thread(monitor, webpage)
		checker.start()
	checker.join()
