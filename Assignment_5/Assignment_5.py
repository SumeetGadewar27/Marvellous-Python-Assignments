#find the Even or Odd Nmber 

a=lambda Value1 : Value1 % 2 == 0

def main():
    Value1=int(input("Enter a number : "))
    
    if  ( a(Value1) ) == True :
        print("-"*48)
        print( Value1," is an Even number. ")
    else :
        print("-"*48)
        print( Value1," is an Odd number. ")
        
    print("-"*48)

if __name__ == "__main__":
    main()