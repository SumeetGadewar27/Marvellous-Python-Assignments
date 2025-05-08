#Assignment 7
def Chknum(num):
    if (num % 5) == 0 :
        print("True ")
    else :
        print("False ")
            
def main():
    number= int(input("Enter the number : "))
    return Chknum(number)
    
if __name__ == '__main__':
    main()