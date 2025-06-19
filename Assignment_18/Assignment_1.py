#Check Weather file is exists or not
# Call :-  python Assignment_1.py Demo.txt
import time
import schedule
import sys
import os 

def header():
    print("~"*56)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n\n")

def footer():
    print()
    print("~"*56)
    print("~"*12,"Thankyou For using our Applicaton","~"*12)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n") 

def FileChecker(File):
    PFile = os.path.abspath(File)
    if os.path.exists(PFile):
        print("File ",File," is exists")
    else:    
        print("File ",File," is not exists")
    

def main():
    header()
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used check file or not. ")
            print("--> This is to check file is available or not. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to check file availblity.")
            print("--> ScriptName.py filename.ext of document") 
            print("--> Please Provide valid absolute path") 
        
        else :
            FileChecker(sys.argv[1])

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