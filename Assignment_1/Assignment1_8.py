#Assignment 8
def starline(num):
    for i in range(num):
        print("*",end =' ')
        # print(i,"*",end =' ')
            
def main():
    number= int(input("Enter the number : "))
    return starline(number)
    
if __name__ == '__main__':
    main()