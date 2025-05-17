#Assignment_5
import functools as ft
# User define Functions 
def Prime(Value):
    for i in range(2,Value):
        if (Value % i == 0)  :
            return 
    return Value

def MaxX(Value):
    j=Value[0]
    for i in Value:
        if  j < i :
            j=i 
    return j
    
def FMR(List):
  
    ListF=list(filter(Prime,List)) #Primenumber
    print(ListF)
   
    # lmm=lambda a : a * 2
    ListM=list(map(lambda a : a*2 ,ListF))   # multiple by 2
    print(ListM)

    # lmr=lambda a,b : a < b
    # ListR=ft.reduce(MaxX,ListM) #Error 
 
    ListR=(MaxX(ListM))    #find max number is 62/31
    print(ListR)

# Main Call 
def main():
    List = [2,70,11,10,17,23,31,77]  # Input 

    print(List)             #1st to start  
    FMR(List)               #2nd to Call

# Starter 
if __name__ == "__main__":
    main()