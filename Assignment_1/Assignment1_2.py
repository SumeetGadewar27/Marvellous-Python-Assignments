# Assignment 2  
def ChkNum(number):         # step 3
    if number % 2 == 0:
        print("Even Number")
    else: 
        print("Odd Number") 


def main():                 #step 2 
    num=int(input("Enter the number : "))
    return ChkNum(num) 
  

if __name__ == '__main__':  #start of execution Step 1
    main()