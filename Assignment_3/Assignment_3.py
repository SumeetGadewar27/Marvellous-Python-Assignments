#Assignment_3
import sys as s
def main():
    Count=int(input("Number of Element : "))
    List=[]
    for i in range(Count):
        element=int(input())
        List.append(element)
    #List=[130,133,5,45,7,2,43,3444,156,4,56,5,34,2,2,1,5,65,100]

    k=List[0]   
    for i in List:
        if i < k:
            k=i
            
    print("Minimum ", k)
 
if __name__ == "__main__":
    main()

