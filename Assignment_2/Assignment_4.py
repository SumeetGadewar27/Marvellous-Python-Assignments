import Arithmetic as ar
#Factor Additon 
def factorAdd(a):
    fact=0
    for i in range(1,9) :
        if (a % i == 0 ):
            fact=fact+i
    return fact

def main():
    print("")
    Value1=int(input("Enter Number for Factor : "))
    
    print(factorAdd(Value1))
    
    # print(ar.fact(Value1)) #using module
        
 
if __name__ == "__main__":
    main()
