#Print cube and SQuare 

Square = lambda v : v ** 2 
Cube = lambda v : v ** 3
   
def main():
    print("~"*70)

    Value=int(input("Enter a number: "))
    print("Square: ",Square(Value))
    print("Cube  : ",Cube(Value))

if __name__=="__main__":
    main()