#Assignment 1  -- Sum of list
import MarvallousNum as mn
def main():
    List=mn.numberCall()
    # List=[13,5,45,7,4,56]
    # print(max(List))
    sum=0   
    for i in List:
        sum=sum+i

    print(sum)
 
if __name__ == "__main__":
    main()

