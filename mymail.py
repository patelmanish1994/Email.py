import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "manishkumarpatel1994@gmail.com"
toaddr = "manishkumarpatel1994@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] ='manishkumarpatel1994@gmail.com'
msg['To'] = 'manishkumarpatel1994@gmail.com'
msg['Subject'] = "your data here for the first file"
 
body = "data of the student"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "ABHIROOP TAYAL.txt"
attachment = open("C:\Users\\manish\\Downloads\ABHIROOP TAYAL.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "manish007")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()