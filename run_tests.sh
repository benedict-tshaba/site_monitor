#!/bin/bash

python -m unittest tests.site_monitor_test
rm logs/website_changes.log logs/hashes.db

touch logs/website_changes.log
touch logs/hashes.db
