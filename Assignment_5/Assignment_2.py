def Vowels(Value1):

    Vowel=["a","e","i","o","u",'A', 'E', 'I', 'O', 'U']

    if Value1  in Vowel :
        print("-"*48)
        print( Value1," is a vowel. ")
    else :
        print("-"*48)
        print( Value1," is a consonant. ")


def main():
    Value1=input("Enter a character : ")
    
    Vowels(Value1)
    print("-"*48)
    
if __name__ == "__main__":
    main()