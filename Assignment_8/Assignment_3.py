import time as tm 
import threading as td
import functools as ft

ListE = [1,2,3,4,5,6,7,8,9,10,12,13,15,16,17]

def Evelist(ListE):
    EvenListF=list(filter(lambda i : (i % 2 == 0  ),ListE ))
    print(EvenListF)

    EvenListM=ft.reduce( lambda x,y : x + y  ,EvenListF)
    print(EvenListM)
    

def OddList(ListE):
    OddListF=list(filter(lambda a : (a % 2 != 0),ListE ))
    print(OddListF)

    OddListM=ft.reduce( lambda x,y : x + y, OddListF  )
    print(OddListM)

def main():

    thread1 = td.Thread(target=Evelist,args=(ListE, ))
    thread2 = td.Thread(target=OddList,args=(ListE, ))

    thread1.start()
    thread1.join()
    thread2.start()   
    thread2.join()

    end_time=tm.time()
    
    print("  Exit from main.")
    print(end_time-start_time)

if __name__ == "__main__":
    print("~"*50)

    start_time=tm.time()
    print("  Start of main.")
    
    main()

