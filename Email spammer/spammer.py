import smtpd
import smtplib
import time
from email.mime.text import MIMEText
from datetime import datetime

#Acc credentials
adress = "przemolmroz19@gmail.com"
password = "..."
#Recipient
spamEmail = "..."

#counter
count = 0
maxEmails = 20


subjects = [
    "Auto Email {count}",
    "spam"
    "{time}"
]

def send_email(count):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subjects = subjects[count % len(subjects)].format(time = now)
    body = f'This is automatic email #{count + 1} sent at {now}.'
    msg = MIMEText(body)
    msg['Subject'] = subjects
    msg['From'] = adress
    msg['To'] = spamEmail

    try:
        with smtplib.SMTP('smtp.gmail.com', 465) as smtp: #smtp.office365.com, 587
            #smtp.starttls() outlook
            smtp.login(adress, password)
            smtp.send_message(msg)
            print(f'[+] Email #count{count + 1} sent at {now}')
        
        with open("email_log.txt", "a") as log:
            log.write(f'[{now}] Email #{count + 1} sent to {spamEmail} \n')
    
    except Exception as e:
        print(f'[!] Failed to send email #{count + 1}: {e}')

while count < maxEmails:
    send_email(count)
    count += 1
    time.sleep(30)
    
