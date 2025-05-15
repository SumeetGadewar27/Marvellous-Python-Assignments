#Assignment_2  -- To find maximum Number of list
import MarvallousNum as mn 

def maxX(List):
    j=List[0]
    for i in List:
        if i > j:
            j=i

    return j

def main():    
    List=mn.numberCall()   #Function call from Module
    #List=[130,133,5,45,7,2,43,3444,156,4,56,5,34,2,2,1,5,65,100]
    print("Max NUmber is ", maxX(List) )

if __name__ == "__main__": #Starter
    main()

