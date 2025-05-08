#Assignment 6
def Chknum(num):
    if num < 0 :
        print("Negative Number ")
    elif num > 0 :
        print("Positive Number ")
    else :
        print("Zero ")
            
def main():
    number= int(input("Enter the number : "))
    return Chknum(number)
    
if __name__ == '__main__':
    main()