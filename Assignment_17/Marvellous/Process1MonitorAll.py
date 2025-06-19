#Here We are starting for Pcoess
import psutil

def header():
    print("~"*58)
    print("~"*17,"Marvellous Automation","~"*18)
    print("~"*58,"\n\n")

def Footer():
    print("\n\n","~"*57)
    print("~"*13,"ThananYou for ysing Our Script","~"*13)
    print("~"*17,"Marvellous Automation","~"*18)
    print("~"*58) 

def ProcessDisplay():
    print("*"*58)
    print("Information of Currently Running Process : ")   
    print("*"*58)

    for proc in psutil.process_iter():   #  to iterate the Process same as OS.walk()
        info = proc.as_dict(attrs=['pid','name','username']) # as_dict inbuild fuction
        info["vms"]=proc.memory_info().vms / (1024 * 1024) #kb to Mb
        print(info)

def main():
    ProcessDisplay()

if __name__ == "__main__":
    print("@Start of Program")
    header()
    main()
    Footer()
    print("@End of Program")
 
#tasklist Command on CMD to get TaskManager

# >python Process1MonitorAll.py