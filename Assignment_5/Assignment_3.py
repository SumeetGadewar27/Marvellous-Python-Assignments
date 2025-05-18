def Vote(Value1):

    if  Value1 >= 18 :
        print("-"*48)
        print( Value1," Eligible to Vote ")
    else :
        print("-"*48)
        print( Value1," Not Eligible to Vote ")


def main():
    Value1=int(input("Enter age : "))
    
    Vote(Value1)
    print("-"*48)
    
if __name__ == "__main__":
    main()