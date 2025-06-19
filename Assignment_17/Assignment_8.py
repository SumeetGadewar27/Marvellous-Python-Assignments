#Schedule a function to perform file backup every hour and write a log entry 
#into backup_log.txt
# Call :-  python Assignment_8.py
import os 
import time
import schedule
import shutil
import sys
def header():
    print("~"*56)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n\n")

def footer():
    print("~"*56)
    print("~"*12,"Thankyou For using our Applicaton","~"*12)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n") 

def BackUpFolder():
    print("Checking mail...")
    print("At : ",time.ctime())

def main():
    header()
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used check mail. ")
            print("--> This is to check mail and stay updated. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to clean data of file.")
            print("--> ScriptName.py of document") 
            print("--> Please Provide valid absolute path") 
        
    elif ( len(sys.argv) == 1 ):
        schedule.every(10).seconds.do(BackUpFolder)
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("--- Invalid number of Arguments !")
        print("Use the given flag as : ")
        print("--u : Used to display the usage" )       
        print("--h : Used to display the help" )

    footer()

if __name__ == "__main__":
    print("-->@ Start")
    print("*"*50)
    main()
    print("*"*50)
    print("-->@ End")