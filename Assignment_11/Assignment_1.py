#print 1 2 3 4 5 using recurssion 
x=1
def Incremental(a):
    global x
    if  x <= a:
        print(x,end=" ")
        x=x+1
        Incremental(a)
    else:
        return None 
    
def main():
    try:
        a=int(input("Enter a number : "))
        Incremental(a)
    except ValueError : 
        print("Enter the Valid input")
   
    finally :
        print("Program is End ")        
if __name__ == "__main__":
    print("~"*50)
    main()

