# to print the * right triangle using Recursion 
Star=0
def star(x):
    global Star
    Star=Star+1
    if x > 0:
        print(" * " * Star)
        x=x-1
        star(x)
    return ""
        
def main():
    try:
        a=int(input("Enter a number : "))
        print(star(a))

    except ValueError : 
        print("Enter the Valid input")
    
    except TypeError : 
        print("Invalid exrpession ")

    finally :
        print("Program is End ")  
              
if __name__ == "__main__":
    print("~"*50)
    main()