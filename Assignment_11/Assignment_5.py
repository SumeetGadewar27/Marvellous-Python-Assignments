#to print the count of the Given Number
import sys 
count=0
x=0
print
y=0
def ZeroCount(a):
    global count, x, y
    if  (a > 0 ):
        if a % 10 == 0 :
            count=count+1
            y = a//10
            a=y
            ZeroCount(a)
        else:
            y = a//10
            a=y
            ZeroCount(a)
    return count

    
def main():
    try:
        a=int(input("Enter a number : "))
        if len(str(a))==1:
            if (a)==0:
                print("Count Zeros(",a,")-->", 1) 
        else:
            print("Count Zeros(",a,")-->",ZeroCount(a)) 
            sys.setrecursionlimit(100000000)  # used to set the stack of limit ByDefault its 1000 
        
    except ValueError : 

        print("Enter the Valid Numer 0-9")
    
    except TypeError : 
        print("Invalid exrpession ")

    except RecursionError:
        print("Enter the number less then 10000000 ")
    
    except AttributeError:
        print("Enter the Interger value, without Dot(.) or float")

    finally :
        print("Program is End ")  
              
if __name__ == "__main__":
    print("~"*50)
    main()


# a=1020300
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
