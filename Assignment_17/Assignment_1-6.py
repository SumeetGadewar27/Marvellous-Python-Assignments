# Call : python Assignment_1-6.py Marvellos.txt
import time
import schedule
import os
import sys
def header():
    print("~"*56)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n\n")

def footer():
    print("~"*56)
    print("~"*12,"Thankyou For using our Applicaton","~"*12)
    print("~"*17,"Marvallous Infosystem","~"*16)
    print("~"*56,"\n") 

def ScheduleSeconds():  #Assignment_1
    print("Jai Ganesha")

def ScheduleMinutes(): #Assignment_2
    DateTime = time.ctime()
    print("Date and time is : ",DateTime)

def ScheduleHalfHour(): #Assignment_3
    print("Marvellous Infosystem")
    print("Sumeet Do Coding...")

def ScheduleNineMorning(): #Assignment_4
    print("Marvellous Infosystem")
    print("Sir Namaskar...")

def ScheduleFiveMinutes(File="Marvellos.txt"): #Assignment_5
    if os.path.exists(File):
        File=open(File,"a")
        File.write("Cureent Date Time : "+time.ctime()+"\n")
    else:
        File=open(File,"w")
        File.write("Cureent Date Time : "+time.ctime()+"\n")
    File.close()

def FunLunch():  # Assignment_6
    print("Hi, Its lunch time ",time.ctime())
def FunEnd():
    print("Hi, Wreap up work",time.ctime())

def main():
    header()
    if (len(sys.argv) == 2):
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("--> This Application is used to Schedule . ")
            print("--> This is to schedule Seconds/Minutes/Hour/Day. ")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("--> Use the given Script to clean data of file.")
            print("--> ScriptName.py FileName.txt of document") 
            print("--> Please Provide valid absolute path") 
        
        else :
            if os.path.exists(sys.argv[1]):

                schedule.every(2).seconds.do(ScheduleSeconds) #A1
                schedule.every(1).minutes.do(ScheduleMinutes) #A2
                schedule.every(30).minutes.do(ScheduleHalfHour)#A3
                schedule.every().day.at("09:00").to(ScheduleNineMorning)   #4
                schedule.every(5).minutes.do(ScheduleFiveMinutes)   #5
                schedule.every().day.at("13:00").to(FunLunch)   #6.1
                schedule.every().day.at("17:00").to(FunEnd)   #6.2

                while True:
                    schedule.run_pending()
                    time.sleep(1)

            else:
                print("File is not Available in the system.")
                FileName=input("Enter the file name to create : ")
                FileName=open(FileName,"w")      
    else:
        print("--- Invalid number of Arguments !")
        print("Use the given flag as : ")
        print("--u : Used to display the usage" )       
        print("--h : Used to display the help" )
    
    footer()

if __name__ == "__main__":
    print("--->@Start")
    print("~"*50)
    main()
    print("~"*50)
    print("--->@End")