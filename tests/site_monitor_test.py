#!/usr/bin/python

from lib.site_monitor_lib import SiteMon
import time
import unittest
import pickle

sm = SiteMon("logs/hashes.db", "logs/website_changes.log", None)

class SiteMonitorTestCase(unittest.TestCase):

	def test_hasher(self):
		with open('tests/test_data/index.html', 'r') as f:
			data = f.read()
			self.assertEqual(sm.hasher(data), "ea58929928af5ac5e83e365e585b4a57f95e2482cf8c000d285197dab644ab34")

	def test_log(self):
		msg = " -- Test message check -- \n"
		sm.log(msg)
		with open('logs/website_changes.log', 'r') as f:
			log_msg = f.readline()
			self.assertEqual("Date: "+time.asctime()+msg, log_msg) # the log was written

	def test_show_report(self):
		result = sm.show_report()
		with open('logs/website_changes.log', 'r') as f:
			logs = f.read()
			self.assertEqual(result, logs)

	def test_save_checksum(self):
		with open('tests/test_data/index.html', 'r') as f:
			data = f.read()
			hash1 = sm.hasher(data)
			sm.save_checksum('tests/test_data/index.html', hash1)
		fs = file('logs/hashes.db', "rb")
		hash2 = pickle.load(fs)
		self.assertEqual(hash2['tests/test_data/index.html'], hash1)

if __name__ == '__main__':
	unittest.main()
