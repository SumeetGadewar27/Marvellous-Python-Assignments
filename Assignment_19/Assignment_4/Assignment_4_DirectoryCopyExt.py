''' 4. Design automation script which accept two directory names and one file extension. 
Copy all files with the specified extension from first directory into second directory. 
Second directory should be created at run time. 
Usage: Directory CopyExt.py "Demo" "Temp" ".exe"
Demo is name of directory which is existing and contains files in it. 
We have to create new Directory as Temp and copy all files with extension.exe from Demo to Temp.
CALL: python Assignment_4_DirectoryCopyExt.py Demo Temp .exe >>Output.txt
''' 
import schedule
import sys
import os 
import time
import shutil
import diroperation # This user define module.

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

 
def FileRename(Extentaion,ChangeExtentaion):
    dict,NewDict = diroperation.DirectoryCopy(sys.argv[2],sys.argv[1])  # To get the Directory path From UDF Module

    # Log="ExtentationLog"
    LogFile = diroperation.DefLog()       # To get the LogFile, From UDF Module
    LogFile.write("*" * 54 + "\n")
    LogFile.write("~~~~~~~~ List of file with the extentaion : "+Extentaion+" ~~~~~~~\n")
    LogFile.write("~~~~~~~~~~~~~~~~" + time.ctime() + "~~~~~~~~~~~~~~\n")
    LogFile.write("~" * 54 + "\n")

    FileCount=0
    for FolderName, SubFolderName, Filename in os.walk(dict):
        for SubFolderName in SubFolderName:
            if len(SubFolderName) == 0:
                SubFolderName=""
                print(SubFolderName,"  SubFolderName")
            else:
                SubFolderName=SubFolderName
        
        for Filename in Filename:   
                           # Count Files 
            
            PFilename=os.path.join((os.path.abspath(FolderName)),Filename)  # Create the path for old File
            PCopyName=os.path.abspath(NewDict) # Create the path for New File

            if  PFilename.endswith(sys.argv[3]): 
                FileCount = FileCount + 1  
                shutil.copy(PFilename,PCopyName)
                msg= (str(FileCount) + ") " + Filename + "\n" )
                LogFile.write(msg)

    LogFile.close
    print("Log updated. ","\n")

    LogFile.write("~" * 54 + "\n")
    LogFile.write("~~~~~~~~~~~~~~~~~~~~~ End of Logs ~~~~~~~~~~~~~~~~~~~~\n")
    LogFile.write("~~~~~~~~~~~~~~~~" + time.ctime() + "~~~~~~~~~~~~~~\n")
    LogFile.write("*" * 54 + "\n\n")
 
def main():
    header()

    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used for list of files . ")
            print("--> This is to get the list of file with the extentation like csv/pdf/txt etc. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to count the words.")
            print("--> ScriptName.py .ext  of document.") 
            print("--> Please Provide valid absolute path.") 
        
    elif (len(sys.argv) >= 3):

        try :
            FileRename(sys.argv[2],sys.argv[1])  # Extentaion of file 

        except TypeError:
            print("-- Techinal issue, Invalid input. ",TypeError) 

        except ValueError:
            print("-- Techinal issue, Invalid input. ",ValueError)

        except Exception as eobj:  #Root Class of Execption
            print("Exception Ocured : ",eobj)

        finally:
            print("-- Application End.")
    else:
        print("--- Invalid number of Arguments !")
        print("Use the given flag as : ")
        print("--u : Used to display the usage" )       
        print("--h : Used to display the help" )

    footer()    #Footer

if __name__ == "__main__":

    print("-- > @Start ---------------------")
    main()
    print("-- > @End ---------------------")
