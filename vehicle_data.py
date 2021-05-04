import requests
from bs4 import BeautifulSoup
#
# directory = 'https://www.autoevolution.com/cars/volkswagen-golf-gtd-5-doors-2017.html' \
#             '#aeng_volkswagen-golf-gtd-5-doors-2017-20-tdi-6mt-184-hp'

directory = 'https://www.autoevolution.com/cars/toyota-prius-2018.html#aeng_toyota-prius-2018-18l-cvt-92-hp'

# directory = 'https://www.autoevolution.com/cars/toyota-supra-2019.html#aeng_toyota-supra-2019-20l-8at-197-hp'


source = requests.get(directory).text
soup = str(BeautifulSoup(source, 'lxml'))

soup_list = soup.split('<h3>')

for el in soup_list[1:]:
    print(type(el))
    print(BeautifulSoup(el, 'lxml'))
    print('+++'*20)

soup_list = [BeautifulSoup(el, 'lxml') for el in soup_list[1:]]

for soup in soup_list:
    title = soup.find('p')
    # titles = [el.get_text() for el in titles]
    names = soup.find_all('em')
    names = [name.get_text() for name in names]
    values = soup.find_all('dd')
    values = [value.get_text() for value in values]
    print(title.get_text())
    print(names)
    print(values)
# print(f"values {len(values)}")
# print(f"titles {len(titles)}")
#
# for title in titles:
#     j = titles.index(title)
#     print(f"j: {j}")
#     print(title)
#     for i in range(len(values)//len(titles) * j, len(values)//len(titles) * (j+1)):
#         print(i, names[i], end=': ')
#         print(values[i])
#         # i += 1

