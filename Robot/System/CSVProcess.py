# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    CSVProcess.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 01:34:07 by hkono             #+#    #+#              #
#    Updated: 2021/04/22 12:16:01 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv


class Writing(object):

    def __init__(self):
        self.fieldnames = ['NAME', 'COUNT']

    def make_csv(self):
        with open('data.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writeheader()

    def write_csv(self, restaurant, count):
        with open("data.csv", 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerow({'NAME': restaurant, 'COUNT': count})

    def add_csv(self, restaurant, count):
        with open('data.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writerow({"NAME": restaurant, "COUNT": count})

    def update_csv(self, restaurant, count, row_list):
        with open('data.csv', 'w+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            writer.writeheader()
            for i in range(len(row_list)):
                restaurant = row_list[i]['NAME']
                count = int(row_list[i]['COUNT'])
                writer.writerow({'NAME': restaurant, 'COUNT': count})


class Reading(object):

    def __init__(self):
        pass

    def read_csv(self):
        with open('data.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            row_list = [row for row in reader]
        return row_list
