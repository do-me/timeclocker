###################################
# Time clocker - clock in and out #
###################################

# Author: do-me

# script writes current date and time to text file 
# counts  working hours total and salary for current month 
# all standard python libraries

# import os 
# os.chdir(yourpath)

from datetime import datetime
import ctypes  # message box library 

current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S') # get current time in German format, easy to alter
current_year = datetime.now().strftime('%Y') 

# get last date written in file, else assign None (for first empty line)

try:
    last_date = list(reversed(list(open("Time.txt"))))[0][:10] # reverse opened list, double list transformation ugly but necessary
except:
    last_date = None

# write date and time to file, if current date exists already, only write time 
    
if datetime.now().strftime('%d.%m.%Y') == last_date:
    with open('Time.txt','a') as f:
        f.write(datetime.now().strftime(' - %H:%M:%S'))
    # clocking out
    
    workhours=0
    with open('Time.txt','r') as f:
        for i in f:
            if current_year in i: # current must be in current line, else user might have checked out multiple times, so that one entire line remains without date, hence to be ignored. Doesn´t corrupt algorithm
                if datetime.now().strftime('%m.%Y') == i[3:10]: # calculating only for the same month AND same year!
                    time1 = datetime.strptime(i[11:19],"%H:%M:%S") # convert string to time
                    time2 = datetime.strptime(i[22:30],"%H:%M:%S") 
                    diff = time2 - time1 # type is "timedelta"
                    workhours+=diff.total_seconds()/3600
                else:
                    continue # in case the file contains information from multiple years
                                    
            else: # what 
                continue

    # display info box and ask for icecream depending on workhours  
    
    if workhours<160:
        ctypes.windll.user32.MessageBoxA(None, "Clocked out\n\nThis month you have already worked for %.2f hours.\nYou earned %.1f Euros." % (workhours, workhours*15 ),"Python Clocker", 1) # simple message window
    if 160<workhours<180:
        ctypes.windll.user32.MessageBoxA(None, "Clocked out\n\nThis month you have already worked for %.2f hours.\nYou earned %.1f Euros.\nTime to treat yourself!" % (workhours, workhours*15 ),"Python Clocker", 1) # simple message window
    if workhours>180:
        ctypes.windll.user32.MessageBoxA(None, "Clocked out\n\nThis month you have already worked for %.2f hours.\nYou earned %.1f Euros.\nYou worked too much! Get yourself a day off." % (workhours, workhours*15 ),"Python Clocker", 1) # simple message window
                         
else:
    with open('Time.txt','a') as f:
        f.write(datetime.now().strftime('\n%d.%m.%Y %H:%M:%S'))
        ctypes.windll.user32.MessageBoxA(0, "Clocked in", "Python Clocker", 1)
        # clocking in 
