import requests
from bs4 import BeautifulSoup

directory = 'https://www.autoevolution.com/cars/volkswagen-golf-gtd-5-doors-2017.html' \
            '#aeng_volkswagen-golf-gtd-5-doors-2017-20-tdi-6mt-184-hp'

source = requests.get(directory).text
soup = BeautifulSoup(source, 'lxml')

titles = soup.find_all('h3')
titles = [el.get_text() for el in titles]
names = soup.find_all('em')
names = names[2:]
values = soup.find_all('dd')

i = 0
for value in values:
    print(i, names[i].get_text(), end=': ')
    print(value.get_text())
    i += 1

# data = {}
# for title in titles:
