import smtplib
import random
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

log_file = "Verification_log.txt"

def log_message(level, module, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] [{level}] [{module}] - {message}"
    with open(log_file, "a") as log:
        log.write(formatted_message + "\n")

# Function to generate a random verification code
def generate_verification_code():
    return ''.join(random.choices('0123456789', k=6))  # 6-digit code

# Function to send verification email
def send_verification_email(receiver_email, verification_code, contact_name):
    sender_email = 'shouldtheone@mail.ru'
    sender_password = '6pq8QkhvNpK4WBKTAUPX'

    log_message("INFO", "Getting Sender Info", f"Sender: {sender_email}")
    log_message("INFO", "Security Code", f"Verification code: {verification_code}")

    subject = "Literary Society"
    qr_code_image_url = "https://i.ibb.co/Y26Hyzt/Qr-Code-removebg-preview.png"  # URL of the hosted image
    
    html_message = f"""\
    <html>
<head>
    <style>
        body {{
            font-family: Georgia, serif;
            font-size: 18px;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4; /* Set background color for the whole page */
        }}
        .container {{
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #fefefe; /* Set background color for the container */
            background-image: url('https://i.ibb.co/VjRrR06/white-concrete-wall.jpg'); /* URL of the background image */
            background-repeat: repeat; /* Repeat the background image */
        }}
        .header {{
            background-color: #FFF2E1;
            padding: 20px;
            text-align: center;
            border-radius: 10px 10px 0 0;
        }}
        .header img {{
            width: 100%;
            max-height: 200px;
            object-fit: contain;
        }}
        .content {{
            padding: 20px;
        }}
        .footer {{
            background-color: #FFF2E1;
            padding: 10px;
            text-align: center;
            border-radius: 0 0 10px 10px;
        }}
        .payment-option {{
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 15px;
            background-color: #f8f9fa;
        }}
        .payment-option-title {{
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .payment-option-info {{
            margin-top: 10px;
        }}
        .qr-code-container {{
            width: 200px;
            height: 200px;
            border-radius: 10px;
            overflow: hidden;
            margin: 0 auto;
        }}
        .qr-code-image {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://i.ibb.co/CnqvVVT/Whats-App-Image-2024-04-25-at-11-13-57-AM-removebg-preview.png" alt="Logo">
            
        </div>
        <div class="content">
            <p>Dear {contact_name},</p>
            <p>We are thrilled to inform you that upon careful evaluation of your application, you have been selected to participate in the UNESCO Creative Writing Competition. Congratulations!</p>
            <p>Through the UNESCO Creative Writing Competition, the Literary Society brings you a chance to showcase your creative talents and win a cash prize worth <strong>10000 TL</strong>. Additionally, your work stands the chance to be published, granting you recognition on a global scale.<br><br> <strong> What's more?</strong><br> Your participation in this competition will be officially recognized and certified by UNESCO, adding further credibility to your achievements.</p>
            <div class="payment-option">
                <div class="payment-option-title">Turkish Lira (TL) IBAN</div>
                <div class="payment-option-info">
                    <p>IBAN: TR060020500009716676700003</p>
                    <p>Account Holder: SERIF ELASHRY</p>
                </div>
            </div>
            <div class="payment-option">
                <div class="payment-option-title">QR Code</div>
                <div class="payment-option-info">
                    <div class="qr-code-container">
                        <img class="qr-code-image" src="{qr_code_image_url}" alt="QR Code">
                    </div>
                    <p>Please scan the QR code provided to complete the payment.</p>
                </div>
            </div>
            <div class="payment-option">
                <div class="payment-option-title">US Dollar (USD) IBAN</div>
                <div class="payment-option-info">
                    <p>IBAN: TR060020500009716676700003</p>
                    <p>Account Holder: SERIF ELASHRY</p>
                </div>
            </div>
            <p>To finalize your application and seize this incredible opportunity, we kindly ask you to complete the application payment.</p>
        </div>
        <div class="footer">
            <p>The Literary Society, <br> Wishes you the best of luck!</p>
        </div>
    </div>
</body>
</html>
    """

    try:
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login(sender_email, sender_password)
        log_message("INFO", "Signing in", "Logged in successfully")

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        part = MIMEText(html_message, 'html')
        msg.attach(part)

        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Verification code sent successfully to", receiver_email)
        log_message("INFO", "Verification Code", f"Verification code sent successfully to {receiver_email}")
    except Exception as e:
        print("Failed to send verification email to", receiver_email, ":", e)
        log_message("ERROR", "Email Sending", f"Failed to send verification email to {receiver_email}: {e}")

# Main function
def main():
    recipients = [
        {"email": "shouldtheone@gmail.com", "name": "Serif"},
        {"email": "abonar213@gmail.com", "name": "abo"},
        # Add more recipients as needed
    ]
    for recipient in recipients:
        receiver_email = recipient["email"]
        contact_name = recipient["name"]
        log_message("INFO", "Receiver Info", f"Received by: {receiver_email}")
        verification_code = generate_verification_code()
        send_verification_email(receiver_email, verification_code, contact_name)
    log_message("INFO", "Process Ended", "Verification process finished\n")

if __name__ == "__main__":
    main()
