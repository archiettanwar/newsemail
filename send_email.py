import ssl
import smtplib
import os

def sendemail(msg):
    host="smtp.gmail.com"
    port=465

    username="archietttanwar71@gmail.com"
    password="newsemailed"

    receiver="archiettanwar71@gmail.com"
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,msg)
