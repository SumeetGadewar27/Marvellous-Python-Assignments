# Display Thread1 and Thread2 , 
import threading as td

def Incremental(no):
    print("Current Thread Active Count : ", td.active_count())
    print("Current name ", td.current_thread().name)
    for i in range(no+1):
        print(i)

def Decremental(no):
    print("Current Thread Active Count : ", td.active_count())
    print("Current name ", td.current_thread().name)
    for i in range(no,0,-1):
        print(i)

def main():
    # no=50
    no=int(input("Enter the number: "))
    # Incremental(no)
    # Decremental(no)

    Thread1=td.Thread(target=Incremental,args=(no,))
    Thread2=td.Thread(target=Decremental,args=(no,))
    print("Thread 1 Execution start ")
    Thread1.start()
    Thread1.join() # wait till finish 
 
    print("Thread 2 Execution start ")
    Thread2.start() # after the T1 Finish T1 will start 
    Thread2.join()

    print("Current Thread Active Count : ", td.active_count())
    print("Current name ", td.current_thread().name)
    
if __name__ == "__main__":
    print("~"*50)
    main()
    