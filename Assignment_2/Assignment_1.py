import Arithmetic as ar

def main():
    print("To Perform arihmetic Operation please enter two numbers.")
    Value1=int(input("Enter 1st Number: "))
    Value2=int(input("Enter 2nd Number: "))

    print("-"*48)
    print("Addition of two number is ",ar.Add(Value1,Value2) )
    print("-"*48)

    print("Substraction of two number is ",ar.Sub(Value1,Value2))
    print("-"*48)

    print("Multiplication of two number is ",ar.Mult(Value1,Value2) )
    print("-"*48)

    print("Division of two number is ",ar.Div(Value1,Value2) )
    print("-"*48)
     
if __name__ == "__main__":
    main()

