from threading import Lock, Thread

file_lock = Lock()

def log(msg):
	with file_lock:
		open('logs/website_changes.log', 'w') as f:
			f.write(msg)

def monitor(webpage):
	""" Monitor the website, if there is a change log it to disk"""

	while True:
		changes = check_for_change(wepage)
		if changes:
			log(changes)

def check_defacement(webpage):
	""" Computes a checksum of the webpage and stores it, on subsequent calls it computes a checksum again and compares it with the one stored on disk if they dont match. Then Possibly the wepage has been defaced."""

	return True

if __name__ == "__main__":
	webpages = ['http://benedict.heliohost.org/', ...]
	for webpage in webpages:
		checker = Thread(monitor, webpage)
		checker.start()
	checker.join()
