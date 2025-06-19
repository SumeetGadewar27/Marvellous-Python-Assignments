#Write a program Student and Enter the 5 stuend names
import os
import sys 
def header():
    print("~"*58)
    print("~"*17,"Marvellous Automation","~"*18)
    print("~"*58,"\n\n")

def Footer():
    print("~"*58,"\n\n")
    print("~"*13,"ThananYou for using Our Script","~"*13)
    print("~"*17,"Marvellous Automation","~"*18)
    print("~"*58) 


def DisplayData(SourceFile):
    if os.path.exists(SourceFile) :
        print("@ File Available ")
        SourceFile=open(SourceFile,"r")

        SourceFile.seek(0)
        Data=SourceFile.read()  
        print(Data)

    else:
        print("File is not Available in the system.")
        FileName=input("Enter the file name to create : ")
        FileName=open(FileName,"w")
        
    # Data=SourceFile.read()    
    # print(Data)
        
def main():
    header()

    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used to to Add Student names. ")
            print("--> This is the student details Script. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script as to Add student names.")
            print("--> ScriptName.py FileName.txt No/Nu of stundent") 
            print("--> Please Provide valid absolute path") 
        
        else : 
           DisplayData(sys.argv[1])      
    else:
        print("--- Invalid number of Arguments !")
        print("Use the given flag as : ")
        print("--u : Used to display the usage" )       
        print("--h : Used to display the help" )
    Footer()
if __name__ == "__main__":
    print("-> @Start","~"*45)
    main()