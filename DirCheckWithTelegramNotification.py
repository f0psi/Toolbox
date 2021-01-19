# 
#	just checks if a new file was created in a specific dir
#	if so a notification will be send with "telegram-send"
# 	befor using you need to setup telegram-send
#	--> https://github.com/rahiel/telegram-send
#
#

import os, time, sys


i=5 #timeoute
pathmon="/path/to/dir/" #path to monitor

def cooldown(x):
        time.sleep(x)


while True:
        print ('\rWaiting for new File    ', end="")
        cooldown(i)
        print ('\rWaiting for new File.', end="")

	#read in filecount
        path, dirs, files = next(os.walk(pathmon))
        file_count = len(files)

        cooldown(i)
        print ('\rWaiting for new File..', end="")
        cooldown(i)
        print ('\rWaiting for new File...', end="")
	
	#read in new file count and check
        path, dirs, files = next(os.walk(pathmon))
        if file_count != len(files):
                os.system("echo 'new File!!' | telegram-send --stdin")

        cooldown(i)