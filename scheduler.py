import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

from config import load_config, save_config


def send_email(subject, body, to_email, config):
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


def send_teams_message(body, config):
    payload = {"text": body}
    try:
        response = requests.post(config['teams']['webhook_url'], json=payload)
        if response.status_code == 200:
            print("Teams message sent successfully")
        else:
            print(f"Failed to send Teams message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send Teams message. Error: {e}")


def send_slack_message(body, config):
    payload = {"text": body}
    try:
        response = requests.post(config['slack']['webhook_url'], json=payload)
        if response.status_code == 200:
            print("Slack message sent successfully")
        else:
            print(f"Failed to send Slack message. Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send Slack message. Error: {e}")


def get_assigned_person(week_number, config):
    if week_number == 1:
        return config['scheduling']['week_1_guy']
    elif week_number == 2:
        return config['scheduling']['week_2_guy']
    elif week_number == 3:
        return config['scheduling']['week_3_guy']
    elif week_number == 4:
        return config['scheduling']['week_1_guy']


def rotate_assignments(config):
    new_config = config.copy()
    new_config['scheduling']['week_1_guy'], new_config['scheduling']['week_2_guy'], new_config['scheduling'][
        'week_3_guy'] = (
        config['scheduling']['week_2_guy'],
        config['scheduling']['week_3_guy'],
        config['scheduling']['week_1_guy']
    )
    return new_config


def main():
    today = datetime.datetime.now()
    week_number = (today.day - 1) // 7 + 1
    current_month = today.month

    # Load current configuration
    config = load_config()

    # Assign the responsibilities
    assigned_person = get_assigned_person(week_number, config)
    responsibilities = "\n".join(
        [f"{idx + 1}. {resp}" for idx, resp in enumerate(config['scheduling']['responsibilities'])])

    subject = "Weekly Responsibilities"
    body = f"Hello ,\n\nYou are assigned the responsibilities for week {week_number}.\n\nResponsibilities:\n{responsibilities}\n\nThank you."

    send_email(subject, body, assigned_person, config)
    send_teams_message(body, config)
    send_slack_message(body, config)

    # Rotate assignments if it's the last week of the month
    last_day_of_month = (datetime.datetime(today.year, today.month + 1, 1) - datetime.timedelta(days=1)).day
    if today.day > last_day_of_month - 7:
        new_config = rotate_assignments(config)
        save_config(new_config)


if __name__ == "__main__":
    main()
