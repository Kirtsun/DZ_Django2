from celery import shared_task

from django.core.mail import send_mail as mail_


@shared_task()
def send_mail(subject, text, from_email):
    mail_(subject, text, 'oleg@gmail.com', [from_email], fail_silently=False)
