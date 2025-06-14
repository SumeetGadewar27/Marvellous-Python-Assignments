#print 1 2 3 4 5 using recurssion 
x=1
b=1
def Incremental(a):
    global x, b
    if  x < a:
        # print(x,end=" ")
        x=x+1
        b=b*x
        Incremental(a)
    return "Factorial of ("+str(a)+ ")--> "+str(b)

def main():
    try:
        a=int(input("Enter a number : "))
        print(Incremental(a))

    except ValueError : 
        print("Enter the Valid input")
    
    except TypeError : 
        print("Invalid exrpession ")

    finally :
        print("Program is End ")  
              
if __name__ == "__main__":
    print("~"*50)
    main()