# Sum of n natiural number using recursion 
import sys

sum=0
def SumNatural(a):
    global sum
    if a > 0:
        sum=sum+a
        a=a-1
        SumNatural(a)
    return sum


def main():
    try:
        a=int(input("Enter a number : "))
        if a > 0:
            sys.setrecursionlimit(100000000)  # used to set the stack of limit ByDefault its 1000 
            print(SumNatural(a)) 
        else: 
            print("Zero 0 is not a natural number")

    except ValueError : 

        print("Enter the Valid Numer 0-9")
    
    except TypeError : 
        print("Invalid exrpession ")

    except RecursionError:
        print("Enter the number less then 10000000 ")

    finally :
        print("Program is End ")  
              
if __name__ == "__main__":
    print("~"*50)
    main()