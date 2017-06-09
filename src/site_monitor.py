from threading import Lock, Thread
import urllib2
import pickle
import time

file_lock = Lock()
hash_dict = {}
hash_file = "logs/hashes.txt"
changes_file = "logs/website_changes.log"

def log(msg):
	with file_lock:
		open(changes_file, 'w') as f:
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
	""" Gets the webpage and returns value of check_defacement"""

    page = urllib.urlopen(webpage)
    return check_defacement(webpage, page.read())

def check_defacement(pagename, data):
	""" Computes a checksum of the webpage and stores it, on subsequent calls
	 it computes a checksum again and compares it with the one stored on disk if they dont match. 
	 Then possibly the wepage has been defaced."""

    known_page_hash = picle.load(hash_file)
    if not known_page_hash[pagename]:
        new_page_hash = md5(data)
        save_checksum(pagename, new_page_hash)
    
    if md5(data) == known_page_hash[pagename]:
        return None

    else:
        msg = "Date: ".time.asctime()
        msg .= "\nThe following ".webpage." might have been maliciosly modified"
        msg .= "\nPlease verify and restore from backup"
    
	return msg

def save_checksum(filename, filehash):
	"""Computes checksum of file, stores it in a dictionary and saves it to disk"""
    
    hash_dict[filename] = filehash
    with open(hash_file) as f:
        #f.write(hashdict)
        pickle.dump(f, hash_dict)

    return None

def md5(data):
    """ returns a hash of the filename given in the argument"""

	file_hash = hashlib.sha1()
	with open(filename, "rb") as f:
		for block in iter(lambda: f.read(4096), b""): # this is premature optimisation. I am assuming that some files
			file_hash.update(block)					  # will be too big to read all at once. but for webpages this is a bit 
	return file_hash.hexdigest()					  # too much?

if __name__ == "__main__":

	webpages = ['http://benedict.heliohost.org/index.html', 'http://benedict.heliohost.org/about.html', 'http://benedict.heliohost.org/', 'http://benedict.heliohost.org/services.html', ...]
	
	for webpage in webpages:
		checker = Thread(monitor, webpage)
		checker.start()
	
	checker.join()
