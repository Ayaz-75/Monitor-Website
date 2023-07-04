import requests
import smtplib
import time
def send_email(sender_email, sender_password, recipient_email, subject, message):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        email_content = f"Subject:{subject}\n\n{message}"
        connection.sendmail(from_addr=sender_email, to_addrs=recipient_email, msg=email_content)

# Website URL to monitor
url = 'https://www.python.org/'

# Email configuration
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
recipient_email = 'recipient_email@example.com'

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website {url} is up and running!")
        else:
            print(f"Website {url} is down! Sending email notification...")
            send_email(sender_email, sender_password, recipient_email, "Website Down", f"The website {url} is currently down.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to access the website: {e}. Sending email notification...")
        send_email(sender_email, sender_password, recipient_email, "Website Down", f"The website {url} is currently down due to an error: {e}.")

    # Adjust the time interval based on your requirements
    time.sleep(300)  # Sleep for 5 minutes
