import requests
from bs4 import BeautifulSoup
from pars.models import Author, Quote


url = "https://quotes.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
for i in soup.find_all('div', {'class': 'quote'}):
    if Author.objects.filter(name=i.small.string):
        r = Author.objects.get(name=i.small.string)
        b = Quote(quote=i.span.string[1:-1], author_id=r.id).save()
    else:
        a = Author(name=i.small.string).save()
        r = Author.objects.get(name=i.small.string)
        b = Quote(quote=i.span.string[1:-1], author_id=r.id).save()
