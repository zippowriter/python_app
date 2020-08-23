import csv
import os

from roboter import function

if os.path.exists('data.csv') is False:
    function.write_first_csv()

# csvファイルの読み込み
with open('data.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    list = [row for row in reader]

# アプリの表側 ------
print('こんにちは！私はRobokoです。あなたの名前はなんですか？')
name = input()

if not list == []:
    list.sort(key=lambda x: x['Count'], reverse=True)
    for i in range(len(list)):
        recommend = list[i]['Name']
        print('私のおすすめのレストランは{}です'.format(recommend))
        print('このレストランは好きですか？ [Yes/No]or[y/n]')
        ans = input()
        if ans == 'No':
            break
        elif ans == 'no':
            break
        elif ans == 'n':
            break

print('{}さん、どこのレストランが好きですか？'.format(name))
restaurant = input().title()

print('{}さん、ありがとうございました。'.format(name))
print('良い1日を！さようなら。')


# アプリの裏側 ------
# 最初だけ
if list == []:
    count = 1
    function.write_csv(restaurant, count)
# 2回目以降
else:
    flag = 0
    num = 0

    # 回答が重複するか調べる（重複するならflag=1）
    for i in range(len(list)):
        if restaurant == list[i]['Name']:
            flag = 1
            num = i
    # 重複しない場合
    if flag == 0:
        count = 1
        function.add_csv(restaurant, count)
    # 重複する場合
    elif flag == 1:
        count = int(list[num]['Count']) + 1
        dict = {'Name': restaurant, 'Count': count}
        list[num] = dict
        # 更新
        function.update_csv(restaurant, count, list)
