#one lambda function and return its power
def main():
    a=lambda x, y : x * y
    
    no1=int(input("Enter 1st number : "))
    no2=int(input("Enter 2nd number : "))

    print("Multiplication : ",a(no1,no2))

if __name__ == "__main__":
    print("~"*50)
    main()