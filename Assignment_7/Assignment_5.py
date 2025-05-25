#Print product the number using resuce
def Palindrome(Value):
    Value2=""
    
    for i in range(len(Value)-1,-1,-1):
        Value2=Value2+Value[i]

    if Value == Value2:
        print(Value," is a Pallindrome ") 
    else:
        print(Value," is a Not Pallindrome ") 
     
def main():  #main Function
    print("~"*50)
    
    Value=input("Enter a string: ")
    
    Palindrome(Value)   #Function Call

if __name__ == "__main__":
    main()