#check weather the File is Exists or not
import os

def main():
    FileName= input("Enter the FileName to Check")
    # FileName=os.path.exists(FileName)
    if os.path.exists(FileName):
        print("File is Available in the system ")
    else:
        print("File is not Available in the system, Please enter the Corret file name.ext ")
        

if __name__ == "__main__":
    print("@Start","~"*45)
    main()

