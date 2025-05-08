#Assignment 9
def even(num):
    i=0
    while i < (num*2):
        i=i+1
        if i%2 == 0:
            print(i, end = " ")

            
def main():
    number= int(input("Enter the number : "))
    return even(number)
    
if __name__ == '__main__':
    main()