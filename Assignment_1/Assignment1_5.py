#Assignment 5
def loop(num):
    for i in range(num,0,-1):
        print(i,end=' ')

def main():
    number= int(input("Enter the number : "))
    return loop(number)
    
if __name__ == '__main__':
    main()