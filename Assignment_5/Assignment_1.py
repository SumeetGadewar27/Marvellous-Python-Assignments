#find the Even or Odd Nmber 

Sum      = lambda Value1,Value2 : ( Value1 + Value2 )
Diff     = lambda Value1,Value2 : ( Value1 - Value2 )
Product  = lambda Value1,Value2 : ( Value1 * Value2 )
Division = lambda Value1,Value2 : ( Value1 / Value2 ) 

def main():
    Value1=int(input("Enter first number  : "))
    Value2=int(input("Enter second number : "))

    print("-"*48)

    print(" Sum :        ",Sum(Value1,Value2) ) 
    print(" Difference : ",Diff(Value1,Value2) )    
    print(" Product :    ",Product(Value1,Value2) ) 
    print(" Division :   ",Division(Value1,Value2) ) 

    print("-"*48)

if __name__ == "__main__":
    main()
