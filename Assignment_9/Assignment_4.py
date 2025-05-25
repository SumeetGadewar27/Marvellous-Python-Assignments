#Compare multiprocess MultiCore and treading
import multiprocessing as mp
import threading as td
import time as tm
import sys
import os

def Sum(no):
    Sum=0
    for i in range(1,no):
        Sum=Sum+i
    # print("The Process id is :",os.getpid())
    # print(Sum)
    return Sum


def main():
    no=[1000000000,0]
    # no=1000000000
    ProcPool=mp.Pool()
    Proc=ProcPool.map(Sum,no) #78. 76
    print(Proc)
  #-------------------
    # Process=mp.Process(target=Sum,args=(no,)) #78. 1
    # Process.start()
    # Process.join()
  #-------------------  
    # Thread1=td.Thread(target=Sum,args=(no,)) #77. 76
    # Thread1.start()
    # Thread1.join()
  #-------------------
    # print(Sum(no) )   # 66.80 sec


if __name__ == "__main__":
    print("~"*50)
    Start_time=tm.time()
    main()
    End_time=tm.time()
    print("Total time : ",End_time-Start_time)