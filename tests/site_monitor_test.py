#!/usr/bin/python

from src.lib.site_monitor_lib import SiteMon
import time
import unittest

sm = SiteMon("logs/hashes.txt", "logs/website_changes.log")

class SiteMonitorTestCase(unittest.TestCase):

	def test_hasher(self):
		with open('tests/test_data/index.html', 'r') as f:
			data = f.read()
			self.assertEqual(sm.hasher(data), "d6ce37718229eaac245a11764d5f4850cca2ec52")

	def test_log(self):
		msg = " -- Test message check -- \n"
		sm.log(msg)
		with open('logs/website_changes.log', 'r') as f:
			log_msg = f.readline()
			self.assertEqual("Date: "+time.asctime()+msg, log_msg) # the log was written

if __name__ == '__main__':
	unittest.main()
