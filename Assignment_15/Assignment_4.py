import os
import sys 
def DataCompare(SourceFile,SourceFile2):
    if os.path.exists(SourceFile) and os.path.exists(SourceFile2):
        print("File Available ")
        SourceFile=open(SourceFile,"r")
        Data=SourceFile.read()
        print("__First file Data  ")
        print(Data)
        
        SourceFile2=open(SourceFile2,"r")
        Data2=SourceFile2.read()
        print("__Second file Data  ")
        print(Data2)

        if Data == Data2:  
            print("Compare Content of ",sys.argv[1]," and ",sys.argv[2])
            print("-- Data Match --")
        else :
            print("Compare Content of ",sys.argv[1]," and ",sys.argv[2])
            print("-- Data not Match --")
    else :
        print("Please enter the valid name of file")

def main():

    DataCompare(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    print("-> @Start","~"*45)
    main()