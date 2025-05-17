#Assignment_2
def main():
    print("To Perform arihmetic Operation please enter two numbers.")
    Value1=int(input("Enter 1st Number: "))
    Value2=int(input("Enter 2nd Number: "))

    r = lambda a,b  : a * b   

    print("-"*48)
    print("Output ", r(Value1,Value2) )
    print("-"*48)

if __name__ == "__main__":
    main()