''' 1. Design automation script which display information of running processes as its name, PID, Username.
Usage: ProcInfo.py 
Call : >python Assignment_1_ProcInfo.py >>Output_A1_ProcInfo.txt  '''
import psutil
import sys
import os 
import time
import schedule
import SumeetDefModule as sd 

def header():
    print("~"*56)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n\n")

def footer():
    print()
    print("~"*56)
    print("~"*11,"Thankyou For using our Applicaton","~"*10)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n") 

def ProcessDisplay():
    # Creating the runtime Log Directory and Log file, Weiting the data.
    LogFile = sd.DefLog("A1_ProcInfo")
    ProcCount = 0
    LogFile.write("~" * 56 + "\n")
    LogFile.write("~" * 5 + " Information of Currently running processess. " + "~" * 5 + "\n") 
    LogFile.write("~" * 10 + " Log Time: " + str(time.ctime() ) + "~" * 11 + "\n")
    LogFile.write("~" * 56+"\n")

    # lising all the current Process 
    for Proc in psutil.process_iter():
        ProcCount = ProcCount + 1
        info = Proc.as_dict(attrs = ['pid', 'name', 'username'])
        # info['vms'] =  Proc.memory_info().vms / ( 1024 * 1024 )
        LogFile.write(str(ProcCount) + ") " + str(info) + "\n")
    
    LogFile.write("~" * 56)
    LogFile.close()
    
def main():
    Pstart = time.time()
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used for track list of current process . ")
            print("--> This is to get the details of proccess details in system. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to get the details of application running .")
            print("--> ScriptName.py Application.exe .") 
            print("--> Please Provide valid absolute path.") 
        
    elif (len(sys.argv) == 1):
            try : 
                schedule.every(5).seconds.do(ProcessDisplay)
                while True:
                    schedule.run_pending()
                    time.sleep(1)
 
            except TypeError:
                print("-- Techinal issue, Invalid input. ",TypeError) 
            except ValueError:
                print("-- Techinal issue, Invalid input. ",ValueError)
            except SyntaxError:
                print("-- Techinal issue",SyntaxError)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as FileAccIssue :
                print("-- Error with file handeling",FileAccIssue)
            except Exception as eobj:  #Root Class of Execption
                print("Exception Ocured : ",eobj)
            finally:
                print("---------------- Application End.-----------------------")
    else:
        print("--- Invalid number of Arguments !")
        print("Use the given flag as : ")
        print("--u : Used to display the usage" )       
        print("--h : Used to display the help" )
    
    Pend = time.time()
    print("~" * 15,"Execution Time : " , str(round((Pend-Pstart),3) ), "~" * 16 )

if __name__ == "__main__":
    header()
    main()
    footer()
