#Assignment_4
import functools as ft
def FMR(List):
    # lmf=(lambda a : (a % 2 == 0) )
    ListF=list(filter(lambda a : (a % 2 == 0),List))
    print(ListF)

    # lmm=lambda a : a + 10
    ListM=list(map(lambda a : a**2 ,ListF))
    print(ListM)

    # lmr=lambda a,b : a * b
    ListR=ft.reduce(lambda a,b : a + b,ListM)
    print(ListR)

def main():
    List = [5,2,3,4,3,4,1,2,8,10]
    print(List) #1st to start 

    FMR(List) #2nd to Call

if __name__ == "__main__":
    main()
