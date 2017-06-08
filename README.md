site_monitor is a Python script that monitors your webpages for any defacements.It does this by first computing checksums of your webpages on first deployment and the subsequently, it will compute the checksum again and compare it with the one it has in the database.

Ideally, the script should be run on a different computer from your webserver, so that in the event your webserver is compromised, the functionality of the program will remain intact and cannot be tempered with.

The program will periodically check the website for modifications, so it goes without saying that if you update your website/wepages you should also update the checksums, otherwise the program will report the modification. I hope to make the program to "self-heal" that is if the website has been defaced the program will restore it from a backup.

TODO:
- Move most of the global variables to a config file.
- Clean up the code a bit
- Document
