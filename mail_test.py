from datetime import datetime
import smtplib
from email.mime.text import MIMEText

data = open('hpc_id_pw_check').readlines()  
data = [line.rstrip('\n') for line in data]   
ip1 = 'cwhpc.lge.com'
id = str(data[0])                                          
pw = str(data[1])  

def mail_sending():
    now = datetime.now()
    now_time = now.time()

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()  # TLS 사용시 필요
    smtp.login('skyiling4', '#c01020667742jy')
    
    msg = MIMEText(' ')
    msg['Subject'] = id + '+ hpc file upload is playing at ' + str(now_time)
    smtp.sendmail('skyiling4@gmail.com', 'jaeyoung.choi@lge.com', msg.as_string())
    smtp.quit()