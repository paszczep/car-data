from constans import FUEL_DESIGNATORS
import requests
import csv
from bs4 import BeautifulSoup


directories = [
    'https://www.autoevolution.com/cars/volkswagen-golf-gtd-5-doors-2017.html'
    '#aeng_volkswagen-golf-gtd-5-doors-2017-20-tdi-6mt-184-hp',
    'https://www.autoevolution.com/cars/volkswagen-arteon-2020.html'
    '#aeng_volkswagen-arteon-2020-20l-tsi-4motion-8at-awd-268-hp',
    'https://www.autoevolution.com/cars/volkswagen-arteon-r-2020.html#aeng_volkswagen-arteon-2020-20l-8at-awd-218-hp',
    'https://www.autoevolution.com/cars/toyota-prius-2018.html#aeng_toyota-prius-2018-18l-cvt-92-hp',
    'https://www.autoevolution.com/cars/toyota-supra-2019.html#aeng_toyota-supra-2019-20l-8at-197-hp',
    'https://www.autoevolution.com/cars/mercedes-benz-e-class-w213-2020.html#'
    'aeng_mercedes-benz-e-class-w214-2020-220d-4matic-9at-194-hp',
    'https://www.autoevolution.com/cars/tesla-motors-model-y-2019.html#aeng_tesla-motors-model-y-2019-60-kwh',
    'https://www.autoevolution.com/cars/volvo-v90-2019.html#aeng_volvo-v90-2019-20l-t4-8at-190-hp',
    'https://www.autoevolution.com/cars/volvo-xc90-2019.html#aeng_volvo-xc90-2019-20l-t5-8at-awd-250-hp',
    'https://www.autoevolution.com/cars/volvo-xc40-recharge-2019.html#aeng_volvo-xc40-recharge-2019-408-hp'
                ]

# with open('information_concerning_a_few_vehicle_variants.csv', 'w', newline='') as csvfile:

total_names = []

for directory in directories:

    source = requests.get(directory).text
    source_split = source.split('<h3>')
    soup_list = [BeautifulSoup(el, 'lxml') for el in source_split[1:]]

    for soup in soup_list:
        title = soup.find('p')
        names = soup.find_all('em')

        for i in range(len(names)):
            if names[i].get_text() in FUEL_DESIGNATORS:
                s = names[i].find_parents('dl').pop().get('title')
                fuel_economy_norm = s[s.find("("):s.find(")")+1]
                names[i] = f'{names[i].get_text()} {fuel_economy_norm}'
            else:
                names[i] = names[i].get_text()

        values = soup.find_all('dd')
        values = [value.get_text() for value in values]
        names.insert(0, 'Name')
        values.insert(0, title.get_text())
        data_dict = {}
        for i in range(len(values)):
            data_dict[names[i]] = {values[i]}
        print()
        for el in data_dict.keys():
            print(el, ' ' * (35 - len(el)), str(data_dict[el])[2:-2])

        total_names += names

print(total_names)
