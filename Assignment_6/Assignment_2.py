#Print sum of 1 to 100  even number 

sum=0
def Loop( no ):

    global sum
    Add=0
    while sum <= no :
        if sum % 2 == 0: 
            Add=Add+sum
        sum=sum+1
    print("While Loop : " ,Add)

    sum=0
    for i in range(no+1):
        if i % 2 == 0:
            sum=sum+i
    print("For Loop   : ",sum)

def main():
    print("~"*50)
    Loop(100) # Function Call

if __name__=="__main__":
    main()