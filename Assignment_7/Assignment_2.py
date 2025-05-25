#Print dobule using map the number
  
def main():
    print("~"*50)
    
    Value=int(input("Enter a number: "))
   
    ListA=[]
    for i in range(Value):
        Valueb=int(input("Enter Values: "))
        ListA.append(Valueb)

    ListM=list(map(lambda x : x * 2,ListA) )  
    print("Doubled list : ",ListM)

if __name__=="__main__":
    main()