import requests
from bs4 import BeautifulSoup

directory = 'https://www.autoevolution.com/cars/volkswagen-golf-gtd-5-doors-2017.html' \
            '#aeng_volkswagen-golf-gtd-5-doors-2017-20-tdi-6mt-184-hp'

source = requests.get(directory).text
soup = BeautifulSoup(source, 'lxml')

titles = soup.find_all('h3')
titles = [el.get_text() for el in titles]
names = soup.find_all('em')
names = [name.get_text() for name in names[2:]]
values = soup.find_all('dd')
values = [value.get_text() for value in values]

for title in titles:
    j = titles.index(title)
    i = 0
    print(title)
    for i in range(len(values)//len(titles) * j, len(values)//len(titles) * (j+1)):
        print(i, names[i], end=': ')
        print(values[i])
        i += 1

# data = {}
# for title in titles:
