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

def DisplayData(Filename):
    Add=input("For Add the Records enter A | For Creating New Records enter W : ")

    if Add == "A" or Add == "a":
        Filename=open(Filename,"a")
        print("Enter the Student name. ")
        for i in range(10):
            print(i+1,") ",end="")
            Filename.write(i+"] ")
            Filename.write(input()+"\n")
            print("")

    elif Add == "w" or Add == "W":
        Filename=open(Filename,"w")
        print("Enter the Student name. ")
        for i in range(10):
            print(i+1,") ",end="")
            Filename.write(input()+"\n")
            print("")

    elif Add == "r" or Add == "R":
        Filename=open(Filename,"r")
        print("List of Stundents  ")
        Filename=Filename.read()
        print(Filename)
    
    else:
        print("Sorry, Invalid Details")
    
def main():
    
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
                DisplayData(sys.argv[1])

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
    print("-> @Start","~"*48)
    header()
    main()
    Footer()