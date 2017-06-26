#!/usr/bin/python

from threading import Lock
import urllib2
import hashlib
import pickle
import time

file_lock = Lock()

class SiteMon(object):
	def __init__(self, hash_file, changes_file):
		self.hash_file = hash_file
		self.changes_file = changes_file
		self.hash_dict = {}


	# logs changes to disk 
	def log(self, msg):
		""" Writes logs to disk, log messages passed (msg) should be in the following format:
		They must be succeeded by a newline character: e.g: 'This is my log message\n' """

		time_stamp = "Date: "+time.asctime()
		with file_lock:
			with open(self.changes_file, 'a+') as f:
				f.write(time_stamp+msg)
		return None

	def hasher(self, data):
		""" returns a hash of the file contents given in the argument"""

		file_hash = hashlib.sha256() #perhaps upgrade to sha512 for more security
		file_hash.update(data)
		return file_hash.hexdigest()

	def save_checksum(self, filename, filehash):
		"""Computes checksum of file, stores it in a dictionary and saves it to disk"""

		self.hash_dict[filename] = filehash

		with open(self.hash_file, 'a') as f:
			pickle.dump(self.hash_dict, f)

		return None

	def show_report(self):
		"""returns the contents of the log file"""
		with open(self.changes_file) as f:
			return f.read()

	# functions for checking the state of my website follow bellow
	def check_defacement(self, pagename, data):
		"""returns a message to be logged if there has been a change in pagename's data since last check"""

		known_page_hash = {}
		try:
			f = file(self.hash_file, "rb")
			known_page_hash = pickle.load(f)
			f.close()
		except: 
			msg = " - Unable to open the hash database"
			return msg

		try:
			if self.hasher(data) != known_page_hash[pagename]:
				msg = "\nThe following "+webpage+" might have been maliciosly modified"
				msg += " - Please verify and restore from backup"
				return msg

		except KeyError: #the page hash is not in our database
			new_page_hash = self.hasher(data)
			self.save_checksum(pagename, new_page_hash)
			msg = " - The page was not in the database, but has since been added"
			return msg

		return None

	def check_availability(self, webpage):
		"""returns a webpage discriptor if page is accessibly, None otherwise"""

		try:
			page = urllib2.urlopen(webpage)
		except urllib2.HTTPError as e:
			return (None, e.code)
		except urllib2.URLError as e:
			return (None, e.reason)

		return (page, None)
