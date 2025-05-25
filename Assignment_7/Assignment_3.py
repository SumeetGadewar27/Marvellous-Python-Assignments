#Print Even the number using filter 
  
def main():
    print("~"*50)
    
    Value=int(input("Enter a number: "))
   
    ListA=[]
    for i in range(Value):
        Valueb=int(input("Enter Values: "))
        ListA.append(Valueb)

    ListM=list(filter(lambda x : x % 2 == 0,ListA) )  
    print("Even Number : ",ListM)

if __name__=="__main__":
    main()