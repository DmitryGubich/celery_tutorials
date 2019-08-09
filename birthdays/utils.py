from django.conf import settings
from django.core.mail import send_mail
from django.template import loader


def send_email_to_me(context):
    html_body = loader.render_to_string('birthdays/mail.html', context=context)
    send_mail(
        subject='Birthday',
        message=html_body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['gubich97@gmail.com'],
        html_message=html_body)
