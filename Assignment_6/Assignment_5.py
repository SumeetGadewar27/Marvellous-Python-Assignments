#Print Prime 

def Prime( no ):
    for i in range(2,no):
        if no % i == 0 :
             return False
    return True
        
def main():
    print("~"*50)

    Value=int(input("Enter a number: "))

    if Prime(Value) == True: # Function Call
        print(Value, " is a Prime number")
    else:
        print(Value, " is not Prime number")

if __name__=="__main__":
    main()