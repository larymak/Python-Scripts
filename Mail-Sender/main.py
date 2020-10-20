import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail():  
    msg = MIMEMultipart()
    msg['Subject'] = 'Subject Here'
    msg['From'] = 'Sender email adress here'
    msg['To'] = 'Receiver email adress here'

    text = MIMEText("Email text here")
    msg.attach(text)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("Email adress here", "Password here")
    s.sendmail("Sender email adress here", "Receiver email adress here", msg.as_string())

sendMail()   
        
