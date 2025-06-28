''' 4. Design automation script which accept directory name and mail id from user and create log file in that directory which contains information of running processes as its name, PID, Username. After creating log file send that log file to the specified mail.
Usage: ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
Demo is name of Directory.
marvellousinfosystem@gmail.com is the mail id. 
Call :- >python Assignment_4_ProcInfoLog.py A4_Demo marvellousinfosystem@gmail.com >>Output_A4_ProcInfoLog.txt'''
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
    # to get the Log file and create the directory at runtime
    LogFile = sd.DefLog(sys.argv[1])
    # add the content in log file
    ProcCount = 0
    LogFile.write("~" * 56 + "\n")
    LogFile.write("~" * 5 + " Information of Currently running processess. " + "~" * 5 + "\n") 
    LogFile.write("~" * 10 + " Log Time: " + str(time.ctime() ) + "~" * 11 + "\n")
    LogFile.write("~" * 56+"\n")

    for Proc in psutil.process_iter():
        info=Proc.as_dict(attrs=['pid','name','username','status'])
        
        if info['status'] == "running":
            ProcCount = ProcCount + 1
            LogFile.write(str(ProcCount) + str(info) + '\n' )
            
    LogFile.write("~" * 56)
    LogFile.close()

    LogFile= LogFile.name
     
    # Declare all Veriables and the Values 
    subject = "[Practice] : Assignment_20 Q_4"
    body = "Jai Shree Ganesh, Ganpati Bappa Morya \n\n" + "RID : PM22000264\n\n"+"Marvellous Programming, Only Coding. \n\n #nustaProgram #nustaCoding \n\n" + str(time.ctime()) + "\n\n Have a great day !"
    sender_email = "sumeetgadewarmarvellous45@gmail.com"
    recipient_email =  sys.argv[2] #"sumeetgadewarmarvellous45@gmail.com", "Sumeetgadewar@yahoo.com"
    sender_password = "seyjtyugdgzoqoss"
    # subject,body,sender_email,sender_password,recipient_email,LogFile = None
    MailSent = sd.usersendmail(subject,body,sender_email,sender_password,recipient_email,str(LogFile))   # From Sum
    print(MailSent)
    


def main():
    Pstart = time.time()
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used for track list of current process . ")
            print("--> This is to get the details of given proccess details in system. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to get the details of application running .")
            print("--> ScriptName.py Application.exe .") 
            print("--> Please Provide valid absolute path.") 
        
    elif (len(sys.argv) == 3):
        try :
            ProcessDisplay()
            # schedule.every(1).hours.do(ProcessDisplay)
            # while True:
            #     schedule.run_pending()
            #     time.sleep(1)

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
