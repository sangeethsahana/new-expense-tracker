import smtplib
#import sendgrid
import os
#from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "ALERT FROM MONEYDEED$"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
#    print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("sahasep30@gmail.com", "sarcasm@1830")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("sahasep30@gmail.com", email, message)
    s.quit()