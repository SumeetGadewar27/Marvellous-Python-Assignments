#Accept the File name from user and show the Contecnt of the file. 
import os

def main():
    
    FileName= input("Enter the FileName to Check : ")
    # FileName=os.path.exists(FileName)
    if os.path.exists(FileName):
        print("File is Available in the system.")
        FileName=open(FileName,"r")
        print(FileName.read())
    else:
        print("File is not Available in the system.")
        FileName=input("Enter thr file name to create : ")
        FileName=open(FileName,"w")
        Content=input("Type here you want to insert the data here.")
        FileName.write(Content)
        

if __name__ == "__main__":
    print("-> @Start","~"*45)
    main()

