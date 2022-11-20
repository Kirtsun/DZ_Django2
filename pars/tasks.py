from celery import shared_task
import requests
from bs4 import BeautifulSoup
from pars.models import Author, Quote

from django.core.mail import send_mail as mail_


@shared_task()
def send_mail(subject, text, to_email):
    mail_(subject, text, 'oleg@example.com', [to_email], fail_silently=False)


@shared_task()
def pars():
    max_page = 15
    count = 0
    url = "https://quotes.toscrape.com/page/1"
    flag = True
    while flag:
        for p in range(max_page):
            r = requests.get(url)
            quotes = BeautifulSoup(r.text, "html.parser")
            if r.status_code != 200 or count >= 5:
                flag = False
                break
            else:
                for q in quotes.find_all('div', {'class': 'quote'}):
                    if count >= 5:
                        flag = False
                        break
                    if not Quote.objects.filter(quote=q.span.string).exists():
                        count += 1
                        author = Author.objects.get_or_create(name=q.small.string)
                        Quote.objects.create(quote=q.span.string, author_id=author[0].id)
                if quotes.find('li', {'class': 'next'}):
                    url = 'https://quotes.toscrape.com/page/' + str(p + 2)
                else:
                    flag = False
                    break
    if count < 5:
        send_mail(subject='Quote', text='Quotes are over', to_email='Oleg@gmail.com')

