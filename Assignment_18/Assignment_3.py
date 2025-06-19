#Copy Data from one file to Another file
# Call :-  >python Assignment_3.py Demo.txt ABC.txt
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

def FileChecker(Source,Destination):
    PSource= os.path.abspath(Source)
    if os.path.exists(PSource):
        PSource=open(PSource,"r")

        print("-------------- Data is copied to given file.------------")
        print("--------------------------------------------------------")
        Destination=open(Destination,"w")
        Destination.write(PSource.read())
        
    else:    
        print("File ",Source," is not exists")
    

def main():
    header()
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used Copy Data . ")
            print("--> This is to see the data from the document ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to copy data from one file to another document.")
            print("--> ScriptName.py SourceFile.ext CopyFile.ext of document") 
            print("--> Please Provide valid absolute path") 
        
    elif (len(sys.argv) == 3):
        FileChecker(sys.argv[1],sys.argv[2])

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