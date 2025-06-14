import os
import sys 
def DataFind(SourceFile,Word):
    if os.path.exists(SourceFile) :
        print("@ File Available ")
        SourceFile=open(SourceFile,"r")
        Data=SourceFile.read()
        print("Data containing file ")
        print(Data)
        
        Data=Data.split()
        Count = 0

        for i in Data:
            if i == Word:
                Count = Count+1
        print("~"*50)
        print(Count, " of word :" ,Word)

    else:
        print("File is not Available in the system.")
        FileName=input("Enter thr file name to create : ")
        FileName=open(FileName,"w")
        Content=input("Type here you want to insert the data here.")
        FileName.write(Content)
        
def main():

    DataFind(sys.argv[1],sys.argv[2])
    

if __name__ == "__main__":
    print("-> @Start","~"*45)
    main()
