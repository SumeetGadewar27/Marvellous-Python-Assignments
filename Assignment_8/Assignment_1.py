#Print Thrading
import threading as td
import time as tm
Eve=0
def funEven( no ):
    global Eve
    for i in range(no):
        Eve=Eve+2
        print("Even: ",Eve)

Odd=1
def funOdd( no ):
    global Odd
    for i in range(1,no):
        Odd=Odd+2
        print("Odd: ",Odd)
        
def main():
    print("~"*50)
    Value=int(input("Enter a number: "))

    # funEven(Value)
    # funOdd(Value)   #36. for 100000

    t1=td.Thread(target=funEven,args=(Value,))  #35 for Thread
    t2=td.Thread(target=funOdd,args=(Value,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__=="__main__":
    Start_time = tm.time()
    main()
    End_time = tm.time()
    print("Total time :- ",End_time-Start_time)
