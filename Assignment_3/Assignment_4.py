#Assignment 4
import sys as s
def main():
    Count=int(input("Number of Element : "))
    List=[]
    for i in range(Count):
        element=int(input())
        List.append(element)
    # List=[13,5,45,7,4,56,5,34,2,5,65]
    elemet=int(input("Element to Search : "))
    count=0
    for i in List:
        if elemet == i: 
            count=count+1
    print("Element Count : ",count)
 
if __name__ == "__main__":
    main()

