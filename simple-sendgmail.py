import smtplib
from os import environ
from sys import argv
from dotenv import load_dotenv

load_dotenv('.env')


subject = argv[1]
content = argv[2]

msg = 'Subject: {}\n\n{}'.format(subject, content)

email = environ.get('EMAIL')
password = environ.get('PASSWORD')

print(email)
print(password)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.set_debuglevel(1)
server.starttls()
server.ehlo
server.login(email, password)
server.sendmail(email, environ.get('RECIPIENT'), msg)
server.quit()