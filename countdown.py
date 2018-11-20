import time
import sys
import os
t0 = int(sys.argv[1]) # in minutes
t0 = t0 * 60

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        os.system('clear')
        print timeformat
        time.sleep(1)
        t -= 1
    print('Time is up!\n\n\n\n\n')

countdown(t0)