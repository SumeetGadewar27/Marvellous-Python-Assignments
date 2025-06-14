import os
import sys 

def main():
    # SourceFile = input("Enter the filename : ")
    SourceFile = sys.argv[1]
    if os.path.exists(SourceFile):
        print("File Available ")
        SourceFile=open(SourceFile,"r")
        Data=SourceFile.read()
        print("__Source File Data  ")
        print(Data)
        
        Destifile=open("DemoFile.txt","w")
        Destifile.write(Data)
        Destifile=open("DemoFile.txt","r")
        Destifile=Destifile.read()
        print("__Destination File Data  ")
        print(Destifile)

    
        
        
        # print(filename2.read())

if __name__ == "__main__":
    print("-> @Start","~"*45)
    main()
