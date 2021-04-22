# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    roboter.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkono <hkono@student.42tokyo.jp>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/01/31 01:33:55 by hkono             #+#    #+#              #
#    Updated: 2021/04/22 12:16:11 by hkono            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Robot.System import operation


def StartUp(Robo):
    row_list = operation.start(Robo)
    name = operation.input_name()
    if not row_list == []:
        Robo.recommend_system(row_list=row_list)
    operation.ask_which_prefer(Robo, name)
    restaurant = operation.input_restaurant()
    operation.update_csv(row_list, restaurant)
    operation.system_down(Robo, name)
