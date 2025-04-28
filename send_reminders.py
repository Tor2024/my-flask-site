import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import os

# === НАСТРОЙКИ ===
GMAIL_USER = os.environ.get('GMAIL_USER')
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')
FROM_NAME = 'Kreuztaler Werkstatt GmbH'

APPOINTMENTS_PATH = 'data/appointments.json'

# === ФУНКЦИЯ ОТПРАВКИ ===
def send_email(to_email, to_name, date_str, time_str):
    subject = 'Erinnerung an Ihren Termin bei Kreuztaler Werkstatt'
    body = f"""
Sehr geehrter Herr/Frau {to_name},

wir erinnern Sie an Ihren Termin am {date_str} um {time_str} in der Kreuztaler Werkstatt GmbH.

Diese E-Mail-Adresse dient ausschließlich zur Versendung von Terminerinnerungen und wird nicht überwacht. Wenn Sie uns kontaktieren möchten, nutzen Sie bitte die E-Mail-Adresse auf unserer offiziellen Webseite.
"""
    msg = MIMEMultipart()
    msg['From'] = f'{FROM_NAME} <{GMAIL_USER}>'
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, to_email, msg.as_string())

# === ОСНОВНОЙ КОД ===
def main():
    tomorrow = (datetime.now() + timedelta(days=1)).date().isoformat()
    with open(APPOINTMENTS_PATH, encoding='utf-8') as f:
        data = json.load(f)
    for appt in data.get('appointments', []):
        if appt.get('date') == tomorrow:
            client = appt.get('client', {})
            email = client.get('email')
            name = client.get('name')
            time_str = appt.get('time')
            if email and name and time_str:
                try:
                    send_email(email, name, tomorrow, time_str)
                    print(f"Erinnerung gesendet an {email} für {tomorrow} {time_str}")
                except Exception as e:
                    print(f"Fehler beim Senden an {email}: {e}")

if __name__ == '__main__':
    main() 