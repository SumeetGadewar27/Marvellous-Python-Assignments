#Write a program to count the Line,Word and Character 
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

def DisplayLine(SourceFile2):
    SourceFile2=open(SourceFile2,"r")
    FileLine=SourceFile2.readlines()
    # print(FileLine)
    print("Line count : ", len(FileLine))
    SourceFile2.close()


def DisplayWords(SourceFile):
    SourceFile1=open(SourceFile,"r")
    FileLine=SourceFile1.read().split()
    # print(FileLine)
    print("Word count : ",len(FileLine),)
    SourceFile1.close()

def DisplayCharacter(SourceFile2):
    SourceFile2=open(SourceFile2,"r")
    FileLine=SourceFile2.read()
    count=0
    for i in FileLine:
        count=count+1
        
    print("Character  count : ",count,)
    SourceFile2.close()
   
        
    # Data=SourceFile.read()    
    # print(Data)
        
def main():
    header()

    

    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used to get the Details of file. ")
            print("--> This is to get the metadata of the file like Count of Words, lines and Character. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to get the count of words lines and character.")
            print("--> ScriptName.py FileName.txt of document") 
            print("--> Please Provide valid absolute path") 
        
        else :
            if os.path.exists(sys.argv[1]) :
                print("@ File Available ") 
                DisplayLine(sys.argv[1])
                DisplayWords(sys.argv[1]) 
                DisplayCharacter(sys.argv[1]) 
            else:
                print("File is not Available in the system.")
                FileName=input("Enter the file name to create : ")
                FileName=open(FileName,"w")      
    else:
        print("--- Invalid number of Arguments !")
        print("Use the given flag as : ")
        print("--u : Used to display the usage" )       
        print("--h : Used to display the help" )
    Footer()
if __name__ == "__main__":
    print("-> @Start","~"*48)
    main()