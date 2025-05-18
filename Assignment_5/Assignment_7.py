#find the Even or Odd Nmber 

Area      = lambda Value1,Value2 : Value1 * Value2
Perimeter = lambda Value1,Value2 : (Value1 * 2) + (Value2 * 2)

def main():
    Value1=int(input("Enter length : "))
    Value2=int(input("Enter width  : "))

    print("-"*48)

    print(" Area : ",Area(Value1,Value2) ) 
    print(" Perimeter : ",Perimeter(Value1,Value2) ) 

    print("-"*48)

if __name__ == "__main__":
    main()
