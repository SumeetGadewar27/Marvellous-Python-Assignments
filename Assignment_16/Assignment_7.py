#write a program to copy content from source.txt to destination.txt
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

def CopyFile(Source,Destination=("UpdatedMarks.txt")):
    
    Dest=Destination

    Source=open(Source,'r')
    print(len(Source.readline()) )
    Source.seek(len(Source.readline()))

    SRC=Source      #SRC use used to Close the Open File. EBeacuse of Readline it stores data we unable to Close
    
    Source=Source.readlines()
    print("READ:-",Source)

    Destination=open(Destination,"a")

    for i in Source:
        List=i.split()
        if len(List)>0:
            if (int(List[1])) > 75 :
                Destination.write(List[0] + " " + List[1]+"\n")

    print("Updated Data  of marks is Stored in File : ",Dest)    
def main():
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used to Clean data. ")
            print("--> This is to Clean data from one file to another file. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to clean data of file.")
            print("--> ScriptName.py FileName.txt of document") 
            print("--> Please Provide valid absolute path") 
        
        else :
            if os.path.exists(sys.argv[1]):
                print("@File Available ")
                CopyFile(sys.argv[1])

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
