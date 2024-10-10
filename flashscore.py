import configparser
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# headers = {}
headers = {"x-fsign": "SW9D1eZo"}
# Считываем учетные данные
config = configparser.ConfigParser()
config.read("flashscore.cfg")


# Присваиваем значения внутренним переменным
# k_game   = config['Keys']['game']
# k_liga = config['Keys']['liga']
# k_country = config['Keys']['country']
# username = config['Keys']['username']

feed = 'ru'
url = f'https://flashscore.com/{feed}'

def main():
    # feed = 'f_1_-1_3_ru_5'
    # url = f'https://d.flashscore.ru.com/x/feed/{feed}'
    # feed = 'r_1_1'
    # url = f'https://46.flashscore.ninja/46/x/feed/{feed}'
    # feed = 'r_4_1'
    # url = f'https://2.flashscore.ninja/802/x/feed/{feed}'
    response = requests.get(url=url, headers=headers)
    r_text = response.text
    if is_data(r_text):
        prepars(r_text)

def is_data(r_text):
    with open(feed, 'w', encoding='utf8') as outfile:
        print(r_text, file=outfile)
    soup = BeautifulSoup(r_text, 'lxml')
    return True

def prepars(r_text):
    data = r_text.split('¬')

    data_list = [{}]

    for item in data:
        key = item.split('÷')[0]
        value = item.split('÷')[-1]

        if '~' in key:
            data_list.append({key: value})
        else:
            data_list[-1].update({key: value})

    for game in data_list:
        print(game)
        # if 'AA' in list(game.keys())[0]:
        #     date = datetime.fromtimestamp(int(game.get("AD")))
        #     team_1 = game.get("AE")
        #     team_2 = game.get("AF")
        #     score = f'{game.get("AG")} : {game.get("AH")}'

        #     print(date, team_1, team_2, score, sep='/')

    with open(feed+'.json', 'w', encoding='utf8') as outfile:
        json.dump(data_list, outfile, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()