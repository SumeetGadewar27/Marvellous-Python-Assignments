#Print Star * 

def Star( no ):
    FactSum = 1
    for i in range(1,no+1):
        print()
        for j in range(i):
            print(" * ",end ="" )
    
        
def main():
    print("~"*50)

    Value=int(input("Enter a number: "))
    Star(Value) # Function Call

if __name__=="__main__":
    main()