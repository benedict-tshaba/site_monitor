import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from ..src.site_monitor import monitor
import unittest

class TestSiteMonitor(unittest.TestCase):

    def test_check_for_change(self):
        pass

    def test_md5(self):
        pass

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
