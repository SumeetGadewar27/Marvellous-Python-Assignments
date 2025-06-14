#print 1 2 3 4 5 using recurssion 
import functools as ft
def main():
    List=[5,2,3,4,3,4,1,2,8,10]
    ListF=list(filter(lambda x : x%2 == 0 ,List))
    print(ListF)

    ListM=list(map(lambda x : x ** 2 ,ListF))
    print(ListM)

    ListR=ft.reduce(lambda x, y : x + y,ListM)    
    print(ListR)

if __name__ == "__main__":
    print("~"*50)
    main()


