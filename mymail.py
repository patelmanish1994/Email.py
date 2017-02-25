import smtplib
import time
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login("emailaddress","password")
def sendmail():
    
    message="keep faith over yourself every thing will be fine"
    server.sendmail("sender email","receiver email",message)


	
    
sendmail()
print" number of mail has been sent=",x
print"mail has been sent according to your request"
