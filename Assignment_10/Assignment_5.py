# Use Filter, Map, Reduce to print the prime number 
import functools as ft
def Prime(a):
    for i in range(2,a):
        if (a % i == 0):
            return None
    return True 
    
def main():
    List=[2,70,11,10,17,23,31,77]

    ListF=list(filter(Prime,List))

    ListM=list(map( lambda X : X * 2 ,ListF))

    Reduce=(ft.reduce(lambda x, y : x if x > y else y ,ListM))

    print(Reduce)



if __name__ == "__main__":
    print("~"*50)
    main()