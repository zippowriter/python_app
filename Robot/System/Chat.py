# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Chat.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 01:34:17 by hkono             #+#    #+#              #
#    Updated: 2021/04/22 12:16:02 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Robot.System import DLdata


class ToHuman(object):

    def __init__(self):
        self.first_contact = 'こんにちは！私の名前はRobokoです。あなたの名前はなんですか？'
        self.asking = '{}さん。どこのレストランが好きですか？'
        self.recommend_restaurant = "私のおすすめのレストランは{}です"
        self.how_do_you_like = "このレストランは好きですか？ [Yes/No or y/n]"
        self.thank_you = "{}さん、ありがとうございました．"
        self.see_you = "良い1日を！さようなら．"

    def say_hello(self):
        print(self.first_contact)

    def ask_like(self, name):
        print(self.asking.format(name))

    def recommend_system(self, row_list=None):
        row_list.sort(key=lambda x: x["COUNT"], reverse=True)
        for i in range(len(row_list)):
            recommend = row_list[i]["NAME"]
            print(self.recommend_restaurant.format(recommend))
            print(self.how_do_you_like)
            answer = input()
            if answer == "No" or answer == "no" or answer == 'n':
                break

    def say_good_bye(self, name):
        print(self.thank_you.format(name))
        print(self.see_you)
