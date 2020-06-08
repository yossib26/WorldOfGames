import os
import time

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():

    try:
        # sleep for 2 seconds after printing output
        #print("SSSSSSSSSSSSS")
        #time.sleep(2)

        # for windows
        if os.name == 'nt':
            os.system('cls')
        # for mac and linux
        else:
            os.system('clear')
    except:
        print("Error cleaning screen ...")


#screen_cleaner()
