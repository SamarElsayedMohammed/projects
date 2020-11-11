import smtplib

from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('Email sending example using Python. It\'s Simple Text Message')

fromEmail = 'samarelsayedmohammed12345@gmail.com'
toEmail = 'samar.elsayed.19944@gmail.com'

msg['Subject'] = 'Simple Text Message'
msg['From'] = fromEmail
msg['To'] = toEmail

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromEmail, 'samar123elsayed123456789')
s.send_message(msg)
s.quit()