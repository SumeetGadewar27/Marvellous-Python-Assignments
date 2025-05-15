#Assignment 8
def main():
    Value1=int(input("Enter Number to Print pattern : "))
    
    for i in range(Value1+1):
        for j in range(1,i+1):
            print(j,end = " ")
        print("")
     
 
if __name__ == "__main__":
    main()
