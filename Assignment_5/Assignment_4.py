def Vote(Value1,Value2,Value3):

    if  (Value1 >  Value2) and (Value1 >  Value3) :
        print("-"*48)
        print("Lagest Number: ", Value1)
    else :
        if (Value2 > Value3) and (Value2 > Value1) :
            print("-"*48)
            print("Lagest Number: ", Value2)
        else:    
            print("-"*48)
            print("Lagest Number: ", Value3)     


def main():
    print("Enter three numbers")
    Value1=int(input("Enter 1st  : "))
    Value2=int(input("Enter 2nd  : "))
    Value3=int(input("Enter 3rd  : "))
    
    Vote(Value1,Value2,Value3)
    print("-"*48)
    
if __name__ == "__main__":
    main()