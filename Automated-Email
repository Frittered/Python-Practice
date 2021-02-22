import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Another Fritz'
email['to'] = 'f***@**.com'
email['subject'] = 'Completed an Automated Email'
email.set_content('Here I am')

# Reminder that you must enable risky apps on your gmail account to allow smtplib to login 

s = smtplib.SMTP(host = 'smtp.gmail.com', port= 587)
s.ehlo()
s.starttls()
s.login('c***@**.com', '****password')
s.send_message(email)
print('it probably definitely went through')
