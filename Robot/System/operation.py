# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operation.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 01:34:33 by hkono             #+#    #+#              #
#    Updated: 2021/04/22 12:16:10 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

from Robot.System import Chat
from Robot.System import CSVProcess
from Robot.System import DLdata


def start(Robo):
    if not os.path.exists('data.csv'):
        w = CSVProcess.Writing()
        w.make_csv()
    r = CSVProcess.Reading()
    row_list = r.read_csv()
    Robo.say_hello()
    return row_list


def input_name():
    ip = DLdata.InputData()
    name = ip.input_name()
    return name


def ask_which_prefer(Robo, name):
    Robo.ask_like(name)


def input_restaurant():
    ip = DLdata.InputData()
    restaurant = ip.input_restaurant()
    return restaurant


def read_data():
    reader = CSVProcess.Reading()
    data = reader.read_csv()
    return data


def update_csv(row_list, restaurant):
    if row_list == []:
        r = CSVProcess.Writing()
        r.write_csv(restaurant, 1)
    else:
        w = CSVProcess.Writing()
        is_ans = 0
        list_num = 0
        for list_i in range(len(row_list)):
            if restaurant == row_list[list_i]["NAME"]:
                is_ans = 1
                list_num = list_i
        if is_ans == 0:
            w.add_csv(restaurant, 1)
        else:
            count = int(row_list[list_num]["COUNT"]) + 1
            csv_dic = {"NAME": restaurant, "COUNT": count}
            row_list[list_num] = csv_dic
            w.update_csv(restaurant, count, row_list)


def system_down(Robo, name):
    Robo.say_good_bye(name)
