import smtplib

gmail_user = 'ntdk0919917609@gmail.com'
gmail_password = 'Duykhanh1234'

sent_from = gmail_user
to = ['aideptrai8655@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, whats up?\n\n- You'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.quit()

print ('Email sent!')

