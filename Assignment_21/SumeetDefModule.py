'''  This Module is used for the get File Path and hexadecimal Values
Note : The directory should be in Cureent or main program having directory.
'''
import os 
import sys 
# Hashlib to get the Hash Value, like md5 
import hashlib
# All imports below are part of python built packages no need to install any exras
import time 
# smtplib provides functionality to send emails using SMTP.
import smtplib
# MIMEMultipart send emails with both text content and attachments.
from email.mime.multipart import MIMEMultipart
# MIMEText for creating body of the email message.
from email.mime.text import MIMEText
# MIMEApplication attaching application-specific data (like CSV files) to email messages.
from email.mime.application import MIMEApplication

''' The getfile function is to get the files for the given the Directory.
this will return the List of Files '''
def getfile(FolderName="Demo"):
    # Declare the Empty list to store the all file names
    GetFileList=[]      

    if os.path.isabs(FolderName) == False:
        FolderName=os.path.abspath(FolderName)

    if os.path.exists(FolderName) == False:
        print("Directory is not availble. ")
        # exit()

    if os.path.isdir(FolderName)  == False:
        print("This is not directory. ")
        # exit()  

    for FolderName, SubFolderName, FileName in os.walk(FolderName):
        
        for FileName in FileName:
            pfileName= (os.path.join(FolderName, FileName))
            GetFileList.append(pfileName)
            
    return GetFileList

''' The findhexavalue function is to get the hashg value for the given the file.'''
def findhexavalue(file):
    Fileslist =file
    # File path Handeling 
    file = file.replace("'\'","'\\'") 
    # open the file in read binary format 
    file = open(file,'rb')
    # read the file 
    # fobj=file.read()
    # read the file in chunks or small units 
    buffer = file.read(100)

    # choosed the has method as md5/ there are lot of many more 
    hobj=hashlib.md5()

    while len(buffer)>0:
        # Update the hash object with file 
        hobj.update(buffer)
        buffer = file.read(100)
    
    # Print the hexa Value using the hexdigest function 
    return hobj.hexdigest()

""" get the Sorurce And target directory to copy or move the data 
Retrun Path-Source Path-target """
def DirectoryCopy(NewDirectory,Directory="Marvellous"):
    # For Soruce Directory
    if os.path.isabs(Directory) == False:   # To check the absolute path 
        Directory=os.path.abspath(Directory)# if not the create 
    
    if os.path.exists(Directory) == False: # 
        Directory=os.path.abspath(Directory)
    
    if os.path.isdir(Directory) == False:
        print("Incorrect directory name.")
        exit()

    # For New/Copy Directory
    if os.path.isabs(NewDirectory) == False:   # To check the absolute path 
        NewDirectory=os.path.abspath(NewDirectory)# if not the create 
    
    if os.path.exists(NewDirectory) == False: # 
        NewDirectory=os.path.abspath(NewDirectory)
        os.makedirs(NewDirectory)

    return Directory, NewDirectory

''' Generate the Log Directory and file .
Retun the logFile absolute Path'''
def DefLog(LogDir="CopyLogs",LofFile="CopyLog"):

    if os.path.isabs(LogDir) == False:   # To check the absolute path 
        LogDir=os.path.abspath(LogDir)   # if not the create 
    
    if os.path.exists(LogDir) == False: # Create the log Directory  
        LogDir=os.path.abspath(LogDir)
        os.makedirs(LogDir)

    LofFile=LofFile+time.ctime().replace(" ","_").replace(":","_")+".txt" # Create the Log File every time 
    LofFile=os.path.join(LogDir,LofFile)    #To create the Log File in Log directory

    if os.path.exists(LofFile):
        LofFile=open(LofFile,"a")
    else:
        LofFile=open(LofFile,"w") 

    return LofFile

def usersendmail(subject,body,sender_email,sender_password,recipient_email,AttchFile = None):
    # subject = "[Practice] : Assignment_20 Q_4"
    # body = "Jai Shree Ganesh, Ganpati Bappa Morya \n" + str(time.ctime()) + "\n Have a great day !"
    # sender_email = "sumeetgadewarmarvellous45@gmail.com"
    # recipient_email = "Sumeetgadewar@yahoo.com"
    # sender_password = "seyjtyugdgzoqoss"
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    

    path_to_file = AttchFile #'SampleMail2.csv'

    # MIMEMultipart() creates a container for an email message that can hold
    # different parts, like text and attachments and in next line we are
    # attaching different parts to email container like subject and others.
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email
    body_part = MIMEText(body)
    message.attach(body_part) 

    # section 1 to attach file
    file = open(path_to_file,'rb') 
    
    # Attach the file with filename to the email
    message.attach(MIMEApplication(file.read(), Name = (os.path.basename(AttchFile) ) ))

    # secction 2 for sending email
    server = smtplib.SMTP_SSL(smtp_server, smtp_port) 
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

    file.close()
    server.close()

    return "Mail Sent to " + recipient_email