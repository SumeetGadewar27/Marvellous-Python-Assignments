#print Decimal Capital and Digit using 3 Threads
import threading as td
import time as tm

def Capital(String):
    print("Capital Thrade id: ",td.get_ident())
    print("Capital Thrade Name: ",td.current_thread().name)
    print("Capital Thrade : ",td.current_thread())
    print("Capital Thrade : ",td.Thread.getName)
    
    for i in String:
        if i.isupper():
            print(i, end = " ")
    print("-"*20)

def Small(String):
    print("Small Thrade id : ",td.get_ident())
    print("Small Thrade Name: ",td.current_thread().name)

    for i in String:
        if i.islower():
            print(i, end = " ")
    print("-"*20)

def Digit(String):
    print("Digit Thrade id : ",td.get_ident())
    print("Digit Thrade Name: ",td.current_thread().name)

    for i in String:
        if i.isdigit():
            print(i, end = " ")
    print("-"*20)

def main():
    # String = "ABCDabcd12345efghEFGH789agbofpwejkjnABKHBDOHBKSDjkb12442540987t43sd4GE"
    String=input("Enter the String ")
    print(" Main ",td.get_ident())
    print("Main Thrade id: ",td.__name__)
    print("Main Thrade Name: ",td.current_thread().name)
    
    # Capital(String)
    # Small(String)
    # Digit(String)  #16 Time 
    
    TCapital=td.Thread(target=Capital,args=(String,))
    TSmall=td.Thread(target=Small,args=(String,))
    TDigit=td.Thread(target=Digit,args=(String,))

    TSmall.start()
    TSmall.join()

    TCapital.start()
    TCapital.join()
    
    TDigit.start()
    TDigit.join()   


if __name__ == "__main__":
    print("~"*50)
    start_time = tm.time()
    main()
    end_time = tm.time()
    print("Total time: ", end_time-start_time)

    