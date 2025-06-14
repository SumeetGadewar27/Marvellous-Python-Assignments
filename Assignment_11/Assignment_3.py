# sum of digit 1234-->10 using recurssion 
import sys
b=0
c=0
sum=0
"""Used 3 veriable to store values for Reminder , Quetation and Sum """
def SumDigit(a):
    global sum, b, c
    if a > 0 :        
        b = a % 10
        sum = sum+b
        c = a // 10
        a=c
        SumDigit(a)
    return sum

def main():
    try:
        a=int(input("Enter a number : "))
        if a > 0:
            sys.setrecursionlimit(100000000)  # used to set the stack of limit ByDefault its 1000 
            print("Sum_of_Digit(",a,")-->",SumDigit(a)) 
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


# a=1234
# b=0
# sum=0
# b = a % 10
# print(b)
# sum = sum+b
# print(sum)
# c = a // 10
# print(c)
# a=c
# print(a)