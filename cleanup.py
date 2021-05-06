import csv

file = 'information_concerning_allegedly_currently_available_vehicles.csv'

with open(file, newline='') as csv_car_data:
    reader = csv.DictReader(csv_car_data)

    print(reader.fieldnames)