# Assignment 3
def Add(a,b):
    addition=(a+b)
    return addition
    

def main():
    print("Enter 2 numbers for addition.")
    num1=int(input("Enter 1st number : "))
    num2=int(input("Enter 2nd number : "))
    addition = Add(a=num1,b=num2)
    print("Addition is : ",addition)
    
if __name__ == "__main__":
    main()