from src.site_monitor import monitor, md5, log
import unittest

class SiteMonitorTestCase(unittest.TestCase):

    def test_md5(self):
        with open('tests/test_data/index.html', 'r') as f:
		data = f.read()
	self.assertEqual(md5(data), "d6ce37718229eaac245a11764d5f4850cca2ec52")

    def test_log(self):
	msg = " -- Test message check -- "
	log(msg)
        with open('logs/website_changes.log', 'r') as f:
		file_msg = f.read()
	self.assertEqual(msg, file_msg.strip('\n'))

if __name__ == '__main__':
    unittest.main()
