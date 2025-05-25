#Print Table of Number

def Table( no ):
    for i in range(1,11):
        print( no ," x ",i," = ",i*no)

def main():
    print("~"*50)
    Table(7) # Function Call

if __name__=="__main__":
    main()