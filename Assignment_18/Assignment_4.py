#COmpare two File Data
# Call :->python Assignment_4.py Demo.txt Hello.txt
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
    print("~"*11,"Thankyou For using our Applicaton","~"*10)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n") 

def WordCounter(File1,File12):
    File1= os.path.abspath(File1)
    File12= os.path.abspath(File12)
    if os.path.exists(File1) and os.path.exists(File12):

        File1 = open(File1,"r")
        File1 = File1.read()
        # File1 = File1.split()

        File12 = open(File12,"r")
        File12 = File12.read()
        # File12 = File12.split()

        Count=0
        if File1 == File12:
            print("Successfull")
        else:
            print("Failure")

def main():
    header()
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used for Count Words . ")
            print("--> This is to count the Occureance of a word from a file ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to count the words.")
            print("--> ScriptName.py SourceFile.ext Word of document") 
            print("--> Please Provide valid absolute path") 
        
    elif (len(sys.argv) == 3):
        WordCounter(sys.argv[1],sys.argv[2])

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