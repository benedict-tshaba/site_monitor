# site_monitor #

## Tshaba Phomolo Benedict ##
### Email: benedicttshaba[at]gmail.com ###

A Python script that monitors webpages for any defacements.
It does this by first computing checksums of your webpages on first deployment and then subsequently, 
it will compute the checksum again and compare it with the one it has in the database.

Ideally, the script should be run on a different computer from your webserver, so that in the event 
your webserver is compromised, the functionality of the program will remain intact and cannot be tempered with.

The program will periodically check the website for modifications, so it goes without saying that if you update 
your website/wepages you should also update the checksums, otherwise the program will report the modification. 
I hope to make the program to "self-heal" that is if the website has been defaced the program will restore it from a backup.

Now we have support for files, so if you have a file online for example if you have an iso file on your server which people can download you can use this program to keep checking the integrity of the file so that if it changes, then you can replace that file with a new one. So the crackers, cant mess with you without you knowing anymore.
