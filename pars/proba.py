import requests
from bs4 import BeautifulSoup
from pars.models import Author, Quote


url = "https://quotes.toscrape.com/page/"
# res = requests.get(url)
# soup = BeautifulSoup(res.text, "html.parser")
max_page = 15
pop = 0
for p in range(max_page):
    cur_url = url + str(p + 1)
    res = requests.get(cur_url)
    soup = BeautifulSoup(res.text, "html.parser")
    par = soup.find_all('div', {'class': 'quote'})
    if pop == 5:
        break
    for i in range(len(par)):
        pa = par[i]
        if Quote.objects.filter(quote=pa.span.string[1:-1]):
            print('er')
        else:
            if Author.objects.filter(name=pa.small.string):
                r = Author.objects.get(name=pa.small.string)
                Quote(quote=pa.span.string[1:-1], author_id=r.id).save()
                pop += 1
            else:
                Author(name=pa.small.string).save()
                r = Author.objects.get(name=pa.small.string)
                Quote(quote=pa.span.string[1:-1], author_id=r.id).save()
                pop += 1
            if pop == 5:
                break
