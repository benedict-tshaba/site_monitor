from src.site_monitor_lib import SiteMon
import unittest

class SiteMonitorTestCase(unittest.TestCase):
	sm = SiteMon("logs/hashes.txt", "logs/website_changes.log")

    def test_hasher(self):
        with open('tests/test_data/index.html', 'r') as f:
		data = f.read()
	self.assertEqual(sm.hasher(data), "d6ce37718229eaac245a11764d5f4850cca2ec52")

    def test_log(self):
	msg = " -- Test message check -- \n"
	sm.log(msg)
        with open('logs/website_changes.log', 'r') as f:
		file_msg = f.readline()
	self.assertEqual(msg, file_msg)

if __name__ == '__main__':
    unittest.main()
