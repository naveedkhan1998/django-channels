from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os


class Util:
    @staticmethod
    def send_email(data):
        subject = data.get("subject", "")
        body = data.get("body", "")
        to_email = data.get("to_email", "")
        from_email = os.environ.get("EMAIL_FROM", "dtemplarsarsh@gmail.com")

        if subject and body and to_email:
            email = EmailMessage(
                subject=subject, body=body, from_email=from_email, to=[to_email]
            )
            email.send()

    @staticmethod
    def send_html_email(subject, to, path_to_html, context):
        html_content = render_to_string(path_to_html, context)
        text_content = strip_tags(html_content)
        from_email = os.environ.get("EMAIL_FROM", "dtemplarsarsh@gmail.com")

        if subject and to:
            email = EmailMultiAlternatives(subject, text_content, from_email, [to])
            email.attach_alternative(html_content, "text/html")
            email.send()
