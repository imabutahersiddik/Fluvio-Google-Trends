import smtplib
from email.mime.text import MIMEText

def send_notification(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)

if __name__ == "__main__":
    send_notification("Test Notification", "This is a test message.")
