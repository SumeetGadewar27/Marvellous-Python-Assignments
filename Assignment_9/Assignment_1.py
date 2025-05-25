import time as tm
import threading as td

def Print5(a):
    for i in range(1,a+1):
        print(i,end = " ")
    print(" ")

def main():
    print("~"*50)
    a=int(input("Enter the number : "))

    print("Thread execution start time:  ",tm.time())
    T1=td.Thread(target=Print5,args=(a,))
    print("1st Thread execution start time: ",tm.time())
    tm.sleep(5)
    T1.start()

    T2=td.Thread(target=Print5,args=(a,))
    print("2nd Thread execution start time: ",tm.time())
    tm.sleep(5)
    T2.start()

    T3=td.Thread(target=Print5,args=(a,))
    print("3rd Thread execution start time: ",tm.time())
    T3.start()

if __name__ == "__main__":
    main()