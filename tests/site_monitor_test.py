import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from ..src.site_monitor import monitor, md5
import unittest

class SiteMonitorTestCase(unittest.TestCase):

    def test_check_for_change(self):
        pass

    def test_md5(self):
        with open('test_data/index.html', 'r') as f:
		data = f.read()
	self.assertEqual(md5(data), "72957ce8ccd2abf9f64cf5c8d0a875ea114af6d5")

    def test_check_defacement(self):
        pass

    def test_log(self):
        pass

    def test_save_checksum(self):
        pass


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from src.site_monitor import monitor
    else:
        from ..src.site_monitor import monitor

    unittest.main()
