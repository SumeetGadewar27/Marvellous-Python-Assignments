import Arithmetic as ar

def fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact

def main():
    print("")
    Value1=int(input("Enter Number to print star: "))
    
    print(fact(Value1))
    
    # print(ar.fact(Value1)) #using module
        
 
if __name__ == "__main__":
    main()
