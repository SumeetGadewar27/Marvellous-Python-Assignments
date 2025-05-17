#Assignment_1
def main():
    print("To Perform arihmetic Operation please enter two numbers.")
    Value1=int(input("Enter 1st Number: "))

    r = lambda a  : 2 ** a

    print("-"*48)
    print("Output ", r(Value1) )
    print("-"*48)

if __name__ == "__main__":
    main()