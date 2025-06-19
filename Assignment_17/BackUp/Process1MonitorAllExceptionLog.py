#Here We are starting for Pcoess 
import psutil

def header():
    print("~"*58)
    print("~"*17,"Marvellous Automation","~"*18)
    print("~"*58,"\n\n")

def Footer():
    print("\n\n","~"*57)
    print("~"*13,"ThananYou for using Our Script","~"*13)
    print("~"*17,"Marvellous Automation","~"*18)
    print("~"*58) 

def ProcessScan():
    print("*"*58)
    print("Information of Currently Running Process : ")   
    print("*"*58)

    listprocess = []

    for proc in psutil.process_iter():
        try:   #  to iterate the Process same as OS.walk()
            info = proc.as_dict(attrs=['pid','name','username']) # as_dict inbuild fuction
            info["vms"]=proc.memory_info().vms / (1024 * 1024) #kb to Mb
            listprocess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            print("Exception Occured")
    return listprocess

def main():
    Arr = ProcessScan()
    for Value in Arr:
        print(Value)


if __name__ == "__main__":
    print("@Start of Program")
    header()
    main()
    Footer()
    print("@End of Program")
 
#tasklist Command on CMD to get TaskManager

# >C:\Users\u1203282\Documents\Sumeet\Python_InClass_Offline\Automation>python Process1Monitor.py > Process1MonitorAllException.txt