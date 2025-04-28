from celery import Celery
import smtplib
from email.mime.text import MIMEText
from config import SENDER_PASSWORD, SMTP_PORT, SMTP_SERVER, SENDER_EMAIL

from celery_config import celery_app
# celery_app = Celery(
#     "mail_service",
#     broker="redis://localhost:6379/0",
#     backend="redis://localhost:6379/0"
# )

# Task: Send an email
@celery_app.task
def send_email(subject: str, body: str, recipient: str):
    try:
        # Replace these with your SMTP server details
        smtp_server = SMTP_SERVER
        smtp_port = SMTP_PORT
        sender_email = SENDER_EMAIL
        sender_password = SENDER_PASSWORD

        # Create the email message
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())

        return f"Email sent to {recipient} successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"
