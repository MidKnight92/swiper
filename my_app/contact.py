import smtplib
from decouple import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email, item, current_price):
    username = config('USERNAME')
    password = config('PASSWORD')

    
    # Message
    subject = "Swiper - Price Dropped on {item}"
    message = f"Great news!! The price of {item} is now {current_price}. Swipe it while you still can! Thanks for using Swiper"
    from_email = f'Swiper <{username}>'
    
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = email
    txt_part = MIMEText(message, 'plain')
    msg.attach(txt_part)

    msg_str = msg.as_string()

    # Login to smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendemail(from_email, email)
    server.quit()

def send_text():
    pass