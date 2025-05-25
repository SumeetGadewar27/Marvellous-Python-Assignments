#Print product the number using resuce
def Palindrome(Value):
    for i in range(2,Value):
        if Value  % i == 0 :
            return False
    return True
         
     
def main():  #main Function
    print("~"*50)
    
    Value=[10,11,12,13,14,15,16,17]

    listF=list(filter(Palindrome,Value))
    print(listF)

if __name__ == "__main__":
    main()