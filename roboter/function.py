import csv

def write_first_csv():
    with open('data.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()


def write_csv(restaurant, count):
    with open('data.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Name': restaurant, 'Count': count})


def add_csv(restaurant, count):
    with open('data.csv', 'a') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Name': restaurant, 'Count': count})


def update_csv(restaurant, count, list):
    with open('data.csv', 'w+') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(list)):
            restaurant = list[i]['Name']
            count = int(list[i]['Count'])
            writer.writerow({'Name': restaurant, 'Count': count})
