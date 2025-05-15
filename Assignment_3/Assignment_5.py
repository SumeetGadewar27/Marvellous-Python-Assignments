#Assignment_5
import MarvallousNum as mn


def ListPrime(List):
    Listb=[]
    for i in List:             #To check the Number is Prime/Not Prime
        if  mn.ChkPrime(i) == None :       
            Listb.append(i)

    sum=0
    for i in Listb:             #To Perform additon of the Prime Numbers
        sum=sum+i
    return sum

def main():
    List=mn.numberCall()
    # Count=int(input("Number of Element : "))
    # List=[]
    # for i in range(Count):
    #     element=int(input())
    #     List.append(element)

    print("Addition of Prime Number ",ListPrime(List))
    # List=[13,5,45,7,4,56,10,34,2,5,8]

if __name__ == "__main__":
    main()

