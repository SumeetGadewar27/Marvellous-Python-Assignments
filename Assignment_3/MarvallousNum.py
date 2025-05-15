def numberCall():
    Count=int(input("Number of Element : "))
    List=[]
    for i in range(Count):
        element=int(input())
        List.append(element)
    return List



#Assignment_3 Q5
def ChkPrime(a):
    for i in range(2,a) :
        if ( a % i == 0 ):
            return True