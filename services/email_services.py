import smtplib
from email.mime.text import MIMEText


def send_email(receiver_email, subject, body):

    sender_email = "sivakumarmanimegalai89@gmail.com"

    smtp_key = "**********WhqudI"

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:

        server = smtplib.SMTP(
            "smtp-relay.brevo.com",
            587
        )

        server.starttls()

        server.login(
            sender_email,
            smtp_key
        )

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print(f"Email sent to {receiver_email}")

    except Exception as e:

        print("Email sending failed")
        print(e)