#!/bin/bash

python -m unittest tests.site_monitor_test
>logs/website_changes.log
>logs/hashes.txt
