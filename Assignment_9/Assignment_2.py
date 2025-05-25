import multiprocessing as mp

ListS=[]

def Square(ListA):
    for i in ListA:
        ListS.append(i**2)
    print(ListS)

ListA=[2,4,6,8,1,3,5,213435,643412,24435234312345,234,
       23432543545346,23542341241345245,234235345345435]

# print(Square(ListA))
def main():
    
    Pro1=mp.Process(target=Square,args=(ListA,))
    Pro1.start()
    Pro1.join()


if __name__ =="__main__":
    main()