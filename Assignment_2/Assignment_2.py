def main():
    print("")
    Value1=int(input("Enter Number to print star: "))
    for i in range(Value1+1):
        if i ==  Value1:
            for j in range(Value1):
                print(" *"*i)

    
    
if __name__ == "__main__":
    main()
