#write a program to count the words 5 , from line from a file
import sys
import os
def header():
    print("~"*54)
    print("~"*18,"Marvallous Infosystem","~"*18)
    print("~"*54,"\n\n")

def footer():
    print("~"*54)
    print("~"*12,"Thankyou For using our Applicaton","~"*12)
    print("~"*18,"Marvallous Infosystem","~"*18)
    print("~"*54,"\n") 

def WordCount(File):
    File=open(File,'r')
    # File
    count=0
    for i in File:
        if len(i.split()) > 5:
            print(i," (",len(i.split()),")") 


def main():
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used to get the Count of Words greater the 5 . ")
            print("--> This is to get the metadata of the file like Count of Words line by  lines . ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to get the count of words from lines .")
            print("--> ScriptName.py FileName.txt of document") 
            print("--> Please Provide valid absolute path") 
        
        else :
            if os.path.exists(sys.argv[1]):
                print("@File Available ")
                WordCount(sys.argv[1])

            else:
                print("File is not Available in the system.")
                FileName=input("Enter the file name to create : ")
                FileName=open(FileName,"w")      
    else:
        print("--- Invalid number of Arguments !")
        print("Use the given flag as : ")
        print("--u : Used to display the usage" )       
        print("--h : Used to display the help" )

    

    

    

if __name__ == "__main__":
    print("  @Start","~"*45)
    header()
    main()
    footer()
