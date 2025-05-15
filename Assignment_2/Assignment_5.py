import Arithmetic as ar

def Prime(a):
    for i in range(2,a) :
        if ( a % i == 0 ):
            return True

def main():
    print("")
    Value1=int(input("Enter Number for prime : "))  
    # if ar.Prime(Value1) ==True:  #Using Module 

    
    if Prime(Value1) == None:
        print(" It is Prime Number : ",Value1)
    else:
        print("It is Not Prime Number : ",Value1)
        
    # print(ar.fact(Value1)) #using module
        
 
if __name__ == "__main__":
    main()
