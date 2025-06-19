#Schedule a function to perform file backup every hour and write a log entry 
#into backup_log.txt
# Call :-  python .\Assignment_7.py Marvellous BackUp BackUpLog.txt
import os 
import time
import schedule
import shutil
import sys
def header():
    print("~"*56)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n\n")

def footer():
    print("~"*56)
    print("~"*12,"Thankyou For using our Applicaton","~"*12)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n") 

def BackUpFolder(BackUpFolder = "BackUp"):
    # def BackUpS(SourceFolder = "Marvellous",BackUpFolder = "BackUp",BackUpFile = "BackUp_log.txt"):
    BackUpFolder = os.path.abspath(BackUpFolder)    #Backup Folder
    if os.path.exists(BackUpFolder):
        BackUpFolder = os.path.abspath(BackUpFolder)
        BackUpFolder = BackUpFolder + '\\'
        
    else:
        BackUpFolder = os.makedirs(BackUpFolder)
        BackUpFolder = os.path.abspath(BackUpFolder)

    return BackUpFolder

def BackUpFile(BackUpFile = "BackUp_log.txt"):
#  def BackUpS(SourceFolder = "Marvellous",BackUpFolder = "BackUp",BackUpFile = "BackUp_log.txt"):   
    BackUpFile=os.path.abspath(BackUpFile)          #Backup File .py .txt .csv
    if os.path.exists(BackUpFile):
        BackUpFile = open(BackUpFile,"a")
        BackUpFile.write("*"*56+"\n")
        BackUpFile.write("*"*10+"Backup at : "+time.ctime()+"*"*10+"\n")
        BackUpFile.write("*"*56+"\n")
    else:
        BackUpFile=open(BackUpFile,"w")
        BackUpFile.write("*"*56+"\n")
        BackUpFile.write("*"*10+"Backup at : "+time.ctime()+"*"*10+"\n")
        BackUpFile.write("*"*56+"\n")
    
    return BackUpFile

def FileWatcher(SourceFolder = "Marvellous"): 
    FBackUpFolder = BackUpFolder(sys.argv[2])
    FBackUpFile   = BackUpFile(sys.argv[3])
    
    for FolderName, SubFolderName, FileName in os.walk(SourceFolder):
        for SubFolderName in SubFolderName:
            if len(SubFolderName) == 0:
                SubFolderName = ""
            else:
                pass
        
        for FileName in FileName:
            OLDFILE=os.path.join(str(FolderName),FileName)
            OLDFILE=(os.path.abspath(OLDFILE)).replace("\\","\\\\")
            
            FBackUpNewFile=os.path.join(FBackUpFolder,FileName).replace("\\","\\\\")
            
            if os.path.exists(OLDFILE):
                shutil.copy2(OLDFILE, FBackUpNewFile)
                FBackUpFile.write(FileName+"\n")
                

    FBackUpFile.write("*"*56+"\n\n")
    print("Backup taken at : ",time.ctime())

def main():
    header()
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used to Clean data. ")
            print("--> This is to Clean data from one file to another file. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to clean data of file.")
            print("--> ScriptName.py FileName.txt of document") 
            print("--> Please Provide valid absolute path") 
        
    elif ( (len(sys.argv) > 2 )or (len(sys.argv) <= 4 )):
        if os.path.exists(sys.argv[1]):
                
            schedule.every(1).hours.do(FileWatcher,sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)

        else:
            print("File is not Available in the system.")
            FileName=input("Enter the file name to create : ")
            FileName=open(FileName,"w")      
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