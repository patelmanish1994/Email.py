import smtplib
import time
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login("manishkumarpatel1994@gmail.com","manish007")
def sendmail():
    
    message="keep faith over yourself every thing will be fine"
    server.sendmail("manishkumarpatel1994@gmail.com","rajat.vns7088@gmail.com",message)

for x in range(1,5):

	
    time.sleep(15)
    sendmail()
    print" number of mail has been sent=",x
print"mail has been sent according to your request"
