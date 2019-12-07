import smtplib, ssl
import qrcode
from PIL import Image
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart



#The host email
sender_email = "ntdk0919917609@gmail.com"
password = 'Duykhanh1234'

#Make the system can send both image and text
message = MIMEMultipart("alternative")
message["Subject"] = "Your Reserving Information"
message["From"] = sender_email

def Send_Email_Enter(receiver_email,slot,time_start,time_end):
    
    message["To"] = receiver_email
    
    #send the QRCode and the time when the customer enters
    qr=qrcode.make(slot)
    qr.save(slot+'.png')
    image=open(slot+'.png','rb')
    
    text = """
    Hi,
    Time start:"""+time_start+"""
    Time end:  """+time_end+"""
    Your slot: """+slot+"""
    This is your QR CODE
    

    """
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEImage(image.read())

    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

