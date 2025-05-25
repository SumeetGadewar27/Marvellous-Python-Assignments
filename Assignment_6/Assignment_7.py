#Print lagest from Number 

def Largest( no ):

    ListA=[]
    for i in range(no):
        Valueb=int(input("Enter Values: "))
        ListA.append(Valueb)

    A=ListA[0]
    for i in ListA:
        if A < i:
            A = i 
    print("Maximum Number is : ",A)
        
def main():
    print("~"*50)

    Value=int(input("Enter a number: "))
    Largest(Value) # Function Call

if __name__=="__main__":
    main()