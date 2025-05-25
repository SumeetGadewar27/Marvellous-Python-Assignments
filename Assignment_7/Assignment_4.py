#Print product the number using resuce
import functools as ft 
  
def main():
    print("~"*50)
    
    Value=int(input("Enter a number: "))
   
    ListA=[]
    for i in range(Value):
        Valueb=int(input("Enter Values: "))
        ListA.append(Valueb)

    ListM=ft.reduce(lambda x , y : x * y ,ListA) 
    print("Product : ",ListM)

if __name__=="__main__":
    main()