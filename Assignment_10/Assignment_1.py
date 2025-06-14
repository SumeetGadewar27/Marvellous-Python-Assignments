#one lambda function and return its power
def main():
    a=lambda x : x ** 2
    
    no=int(input("Enter the number : "))

    print(a(no))

if __name__ == "__main__":
    print("~"*50)
    main()