import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import datetime
from config import config


def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = config['email']['username']
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(config['email']['smtp_server'], config['email']['smtp_port'])
        server.starttls()
        server.login(config['email']['username'], config['email']['password'])
        text = msg.as_string()
        server.sendmail(config['email']['username'], to_email, text)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")


def send_teams_message(body):
    payload = {"text": body}
    try:
        response = requests.post(config['teams']['webhook_url'], json=payload)
        if response.status_code == 200:
            print("Teams message sent successfully")
        else:
            print(f"Failed to send Teams message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send Teams message. Error: {e}")


def send_slack_message(body):
    payload = {"text": body}
    try:
        response = requests.post(config['slack']['webhook_url'], json=payload)
        if response.status_code == 200:
            print("Slack message sent successfully")
        else:
            print(f"Failed to send Slack message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send Slack message. Error: {e}")


def get_assigned_person(week_number):
    if week_number == 1:
        return config['scheduling']['week_1_guy']
    elif week_number == 2:
        return config['scheduling']['week_2_guy']
    elif week_number == 3:
        return config['scheduling']['week_3_guy']
    elif week_number == 4:
        return config['scheduling']['week_1_guy']


def main():
    today = datetime.datetime.now()
    week_number = (today.day - 1) // 7 + 1
    assigned_person = get_assigned_person(week_number)
    responsibilities = "\n".join(
        [f"{idx + 1}. {resp}" for idx, resp in enumerate(config['scheduling']['responsibilities'])])

    subject = "Weekly Responsibilities"
    body = f"Hello,\n\nYou are assigned the responsibilities for week {week_number}.\n\nResponsibilities:\n{responsibilities}\n\nThank you."

    send_email(subject, body, assigned_person)
    send_teams_message(body)
    send_slack_message(body)


if __name__ == "__main__":
    main()
