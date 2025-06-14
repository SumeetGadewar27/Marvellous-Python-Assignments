#print 1 2 3 4 5 using recurssion 
import functools as ft
def main():
    List=[4,34,36,76,68,24,89,23,86,90,45,70]    

    ListF = list(filter(lambda X : X <= 90 and X >= 70,List))
    
    ListM = list(map(lambda X : (X + 10),ListF))

    ListR = ft.reduce(lambda X, Y : X * Y ,ListM)

    print(ListR)

if __name__ == "__main__":
    print("~"*50)
    main()


