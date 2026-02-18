import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = "your email address"
recipient_email = input("Enter recipient email address: ")
subject = input("Enter email subject: ")
body = "Dear Hiring Manager,\n\nPlease find attached my CV for your consideration.\n\nBest regards,\nJeremiah Ongaga"

# File to attach
filename = "tey.pdf"

# Create message container
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject

# Attach the email body
message.attach(MIMEText(body, 'plain'))


# Open the file in binary mode
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters
encoders.encode_base64(part)

# Add header
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Attach the part to message
message.attach(part)

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "your email address"
smtp_password = "your password here"

# Create secure connection with server and send email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Upgrade the connection to secure
    server.login(smtp_user, smtp_password)
    server.sendmail(sender_email, recipient_email, message.as_string())