#find the Even or Odd Nmber 

F=lambda Value1 : Value1 * (9/5)  + 32 

def main():
    Value1=int(input("Enter the Temperature on Celsius  : "))
    print("-"*48)

    print(Value1," Temperature in Fahrenheit: ",F(Value1),"oF" ) 
    
    print("-"*48)

if __name__ == "__main__":
    main()
