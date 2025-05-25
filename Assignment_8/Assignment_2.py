#Print Thrading Even Odd Factor
import threading as td
import time as tm
Eve=0
def EvenFactor( no ):
    global Eve
    for i in range(1,no+1):
            if (no % i == 0) and (i % 2 == 0):
                Eve=Eve+i
    print("Even: ",Eve)

Odd=0
def OddFactor( no ):
    global Odd
    for i in range(1,no+1) :
        if no % i != 0 and (i % 2 != 0):
            Odd=Odd+i
    print("Odd: ",Odd)
            
def main():
    print("~"*50)
    Value=int(input("Enter a number: "))

    # EvenFactor(Value) # 100000 6.59
    # OddFactor(Value)

    t1=td.Thread(target=EvenFactor,args=(Value,))  #4.86 for Thread
    t2=td.Thread(target=OddFactor,args=(Value,))
    t1.start()
    t2.start()
    t2.join()
    t1.join()


    print("Exit from main !")

if __name__=="__main__":
    Start_time = tm.time()
    main()
    End_time = tm.time()
    print("Total time :- ",End_time-Start_time)
