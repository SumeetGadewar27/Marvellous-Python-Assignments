#Sum of Digits Using Recusion 
sum=1
def PowerFunction(x,y):
    global sum
    if y > 0:
        sum = sum * x
        y = y - 1
        PowerFunction(x,y)
    return sum

def main():
    try:
        a = int(input("Enter the first number of power: "))
        b = int(input("Enter the second number of power: "))
        print("power(",a,",",b,") : ",PowerFunction(a,b))
    except ValueError:
        print("please enter Valid input ")
    finally:
        print("Do you want to try again.. ")
    
    

if __name__ == "__main__":
    main()