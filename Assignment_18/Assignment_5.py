#Copy Data from one file to Another file
# Call :-  >python Assignment_5.py ABC.txt Marvellous
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

def WordCounter(Source,U_Word):
    PSource= os.path.abspath(Source)
    if os.path.exists(PSource):

        PSource=open(PSource,"r")
        PSource=PSource.read()
        PSource=PSource.split()

        Count=0
        
        for i in PSource:
            if i == U_Word:

                Count=Count+1
        print("Count of ",U_Word,": ",Count)    

        print("Count of ",U_Word,": ",PSource.count(U_Word))
        
        
    else:    
        print("File ",Source," is not exists")
    

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