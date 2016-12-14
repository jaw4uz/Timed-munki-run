#!/usr/bin/python

#based on Rmanly's Munki_preflight script https://github.com/rmanly/munki_preflight
#and help from RPhillips and Rmanly. This script should be placed in /usr/local/munki/preflight_abort.d if you are running MunkiReport

from sys import argv
from time import localtime

# 24 hour clock remove the hour(s) you want munki to run            
no_run_hours = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0]

# Monday is 0 and Sunday is 6 remove the day(s) of the week you want munki to run
no_run_days = [0, 1, 3, 4, 5, 6]

now = localtime()

(current_weekday, current_hour, current_min) = now[6], now[3], now[4]

try:
    if argv[1] == 'auto':
        # checks if day of the week is not allowed (this needs to be first in the script to stop munki from running every night)
        if current_weekday in no_run_days:
            exit(1)
        # This checks the hour to stop munki from running any other time then what you designate   
        elif current_hour in no_run_hours:
            exit(1)            
except IndexError:
    # somehow we didn't get passed a runtype
    exit(2)
