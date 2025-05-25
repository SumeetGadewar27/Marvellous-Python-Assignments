#Print 1 to 50 
sum=1
def Loop( no ):
    global sum
    while sum <= no :
        print(sum)
        sum=sum+1

def main():
    print("~"*50)
    Loop(50)

if __name__=="__main__":
    main()