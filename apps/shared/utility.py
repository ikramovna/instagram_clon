import re
import threading
from email.message import EmailMessage

from django.core.mail import EmailMessage

email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
phone_regex = re.compile(r"^9\d{12}$")


def check_email_or_phone(email_or_phone):
    if re.fullmatch(email_or_phone, email_regex):
        email_or_phone = "email"

    elif re.fullmatch(phone_regex, email_or_phone):
        email_or_phone = "phone"

    else:
        data = {
            'success': False,
            'message': 'Email or phone number invalid'
        }

    return email_or_phone

class EmailThread(threading.Thread):

    def __int__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        self.email.send()

class Email:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            to=[data['to_email']]
        )
        if data.get('content_type') == 'html':
            email.content_subtype = 'html'
        EmailThread(email).start()

def send_email(email, code):
    html_content = render_to_string(

    )