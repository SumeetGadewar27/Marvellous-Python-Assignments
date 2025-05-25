#Print Factorial 

def Fact( no ):
    FactSum = 1
    for i in range(1,no+1):
        FactSum=FactSum*i
    print("Factorial of " ,no ," is : ",FactSum)
        
def main():
    print("~"*50)

    Value=int(input("Enter a number: "))
    Fact(Value) # Function Call

if __name__=="__main__":
    main()