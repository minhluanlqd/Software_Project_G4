import smtplib, ssl
import qrcode
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#The host email
sender_email = "ntdk0919917609@gmail.com"
password = 'Duykhanh1234'

#Make the system can send both image and text
message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
def Send_Email_Reserve(receiver_email,cost,time_start,time_end):
##   "duc.dustinnguyen@gmail.com"
    
    
    message["To"] = receiver_email

    #send the cost and the time when customer reserves complete
    text = """
    Hi,
    Time start:"""+time_start+"""
    Time end:  """+time_end+"""
    This is your cost:"""+cost+"""
    We have reduced the money in your account"""

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
Send_Email('ntdk0919917609@gmail.com','101','1','1')
