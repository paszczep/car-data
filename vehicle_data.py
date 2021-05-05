from constans import FUEL_DESIGNATORS, WRITTEN_CSV_COLUMNS
import requests
import csv
from bs4 import BeautifulSoup

# total_names = []

with open('information_concerning_a_few_cars.csv', 'w', newline='') as output_csv:
    csv_writer = csv.DictWriter(output_csv, fieldnames=WRITTEN_CSV_COLUMNS)
    csv_writer.writeheader()
    with open('car_make_links.csv', newline='') as source_csv:
        csv_reader = csv.reader(source_csv)
        next(csv_reader)
        for row in csv_reader:
            car_make, car_model, car_body, car_link = row
            print(car_make, car_model, car_body, car_link)

            source = requests.get(car_link).text
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
                data_dict = {'Make': car_make, 'Model': car_model, 'Body': car_body}
                for i in range(len(values)):
                    data_dict[names[i]] = values[i]
                csv_writer.writerow(data_dict)

    #             total_names += names
    #
    # print(total_names)
