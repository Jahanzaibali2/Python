import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email and SMTP details
smtp_server = 'smtp.gmail.com'  # Your SMTP server
port = 587  # For starttls
sender_email = 'ja252821671@gmail.com'
password = 'knysys@123'
receiver_email = 'jahanzaibalikhawja@gmail.com'

# Create message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = 'Test Email'

# Email body
body = "This is a test email sent using Python."
msg.attach(MIMEText(body, 'plain'))

try:
    # Connecting to the SMTP server
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)  # Log in to your email account
    
    # Sending the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
    
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()  # Close the connection
