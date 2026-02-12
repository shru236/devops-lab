import logging
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging configuration
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def send_email(error_message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        server.sendmail(
            os.getenv("EMAIL"),
            os.getenv("EMAIL"),
            f"Subject: Application Error\n\n{error_message}"
        )
        server.quit()
    except Exception as mail_error:
        logging.error(f"Email sending failed: {mail_error}")

def main():
    try:
        print("Application started")
        
        # Simulated error for testing
        x = 10 / 0
        
    except Exception as e:
        logging.error(str(e))
        send_email(str(e))
        print("Error occurred. Logged and email sent.")

if __name__ == "__main__":
    main()
