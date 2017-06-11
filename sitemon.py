from threading import Thread
import ConfigParser

from src.site_monitor import monitor

config = ConfigParser.ConfigParser()
config.read('config.ini')

hashes = config.get('Files', 'hash_file')
logs = config.get('Files', 'changes_file')

if __name__ == "__main__":

    webpages = ['http://benedict.heliohost.org/index.html', 'http://benedict.heliohost.org/about.html'
    , 'http://benedict.heliohost.org/services.html', ]

    for webpage in webpages:
        checker = Thread(target=monitor, args=[webpage,], hash_file=hashes, changes_file=logs)
        checker.start()
        checker.join()