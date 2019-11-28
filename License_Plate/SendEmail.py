import smtplib, ssl
import qrcode
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender_email = "ntdk0919917609@gmail.com"
receiver_email = "aideptrai8655@gmail.com"
password = 'Duykhanh1234'

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
This is your QR CODE"""

SlotNumber=str(i)+'.png'
Image=open(SlotNumber,'rb')

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEImage(image.read())

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
