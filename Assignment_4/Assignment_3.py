#Assignment_3
import functools as ft
def FMR(List):
    # lmf=(lambda a : (a <= 90 and a >= 70) )
    ListF=list(filter(lambda a : (a <= 90 and a >= 70),List))
    print(ListF)

    # lmm=lambda a : a + 10
    ListM=list(map(lambda a : a + 10,ListF))
    print(ListM)

    # lmr=lambda a,b : a * b
    ListR=ft.reduce(lambda a,b : a * b,ListM)
    print(ListR)

def main():
    List = [4,34,36,76,68,24,89,23,86,90,45,70]
    print(List) #1st to start 

    FMR(List) #2nd to Call

if __name__ == "__main__":
    main()
