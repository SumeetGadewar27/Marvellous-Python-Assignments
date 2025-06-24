''' 2. Design automation script which accept directory name and two file extensions from user. 
Rename all files with first file extension with the second file extenntion.
Usage: DirectoryRename.py "Demo" ".txt" ".doc"
Call: python Assignment_2_DirectoryRename.py Demo txt doc
      python Assignment_2_DirectoryRename.py Demo png jpeg
      python Assignment_2_DirectoryRename.py Demo .exe .msi '''
import schedule
import sys
import os 
import time

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

def DirectoryWatcher(Directory="Marvellous"):

    if os.path.isabs(Directory) == False:   # To check the absolute path 
        Directory=os.path.abspath(Directory)# if not the create 
    
    if os.path.exists(Directory) == False: # 
        Directory=os.path.abspath(Directory)
    
    if os.path.isdir(Directory) == False:
        print("Incorrect directory name.")
        exit()
    
    return Directory

def DefLog(LogDir="RenameLogs",LofFile="RenameLog"):
    LofFile=LofFile+time.ctime().replace(" ","_").replace(":","_") # Create the Log File every time 
      
    LogDir=os.path.abspath(LogDir)   # To Create Log Directory 
    
    LofFile=os.path.join(LogDir,LofFile) #To create the Log File in Log directory

    if os.path.exists(LofFile):
        LofFile=open(LofFile,"a")
    else:
        LofFile=open(LofFile,"w") 

    return LofFile
 
def FileRename(Extentaion,ChangeExtentaion):
    dict=DirectoryWatcher(sys.argv[1])  # To get the Directory path 

    # Log="ExtentationLog"
    LogFile=DefLog()                 # To get the LogFile
    LogFile.write("*"*54+"\n")
    LogFile.write("~~~~~~~~ List of file with the extentaion : "+Extentaion+" ~~~~~~~\n")
    LogFile.write("~~~~~~~~~~~~~~~~" + time.ctime() + "~~~~~~~~~~~~~~\n")
    LogFile.write("~"*54+"\n")

    FileCount=0
    for FolderName, SubFolderName, Filename in os.walk(dict):
        for SubFolderName in SubFolderName:
            if len(SubFolderName) == 0:
                SubFolderName=""
                print(SubFolderName,"  SubFolderName")
            else:
                SubFolderName=SubFolderName
        
        for Filename in Filename:   
            if  Filename.endswith(Extentaion): 
                FileCount = FileCount+1               # Count Files 
                UpdateName=Filename.replace(Extentaion,ChangeExtentaion)  #replace the ext with the new ext
                # os.rename()
                PFilename=os.path.join((os.path.abspath(FolderName)),Filename)  # Create the path for old File
                PUpdateName=os.path.join((os.path.abspath(FolderName)),UpdateName) # Create the path for New File

                os.rename(PFilename,PUpdateName)     # Rename used to 
                
                msg= (str(FileCount) + ") " + Filename + " Updated as :" +UpdateName + "\n" )
                LogFile.write(msg)

    LogFile.close
    print("Log updated. ","\n")

    LogFile.write("~"*54+"\n")
    LogFile.write("~~~~~~~~~~~~~~~~~~~~~ End of Logs ~~~~~~~~~~~~~~~~~~~~\n")
    LogFile.write("~~~~~~~~~~~~~~~~" + time.ctime() + "~~~~~~~~~~~~~~\n")
    LogFile.write("*"*54+"\n\n")
 
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
            FileRename(sys.argv[2],sys.argv[3])  # Extentaion of file 

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
