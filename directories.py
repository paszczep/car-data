import csv
import requests
from bs4 import BeautifulSoup

makes = ['Toyota', 'Mercedes', 'Volvo']

with open('car_make_links.csv', 'w', newline='') as csvfile:
    fieldnames = ['make', 'model', 'body', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for make in makes:
        for page_number in range(1, 10):
            directory = f'https://www.autoevolution.com/search.php?t=cars&s={make}&p={page_number}'

            source = requests.get(directory).text
            soup = BeautifulSoup(source, 'lxml')

            spans = soup.find_all('span')

            for present in spans:
                if "- Present" in present.get_text():
                    body_type = present.previous_sibling.text
                    make_model_link = present.parent.parent.a
                    print(make_model_link.get_text(), body_type, make_model_link['href'])

                    writer.writerow({'make': make,
                                     'model': make_model_link.get_text(),
                                     'body': body_type,
                                     'link': make_model_link['href']})
