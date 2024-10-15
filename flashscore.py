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

feed = 'f_1_0_3_ru_1'
url = f'https://2.flashscore.ninja/802/x/feed/'
# url = f'https://2.flashscore.ninja/802/x/feed/{feed}'

def main():
    # feed = 'f_1_0_3_ru_1'     #   список игр
    # url = f'https://d.flashscore.ru.com/x/feed/{feed}'
    # feed = 'r_1_1'
    # url = f'https://46.flashscore.ninja/46/x/feed/{feed}'
    # feed = 'r_4_1'
    # url = f'https://2.flashscore.ninja/802/x/feed/{feed}'
    # feed = 'fo_1_0_3_ru_1_0'  #   КЭФы
    # url = f'https://2.flashscore.ninja/802/x/feed/{feed}'
    response = requests.get(url=url, headers=headers)
    r_text = response.text
    if is_data(r_text):
        games = prepars(r_text)

def is_data(r_text):
    if r_text.find('<!',0)==1:  #   HTML
        with open(feed+'html', 'w', encoding='utf8') as outfile:
            print(r_text, file=outfile)
        return False
        # soup = BeautifulSoup(r_text, 'lxml')
    return True

def prepars(r_text):
    # if r_text.find('SA',0)==-1:   #   Предположительно блок данных
    if r_text.find('÷',2)==-1:   #   Предположительно блок данных
        with open(feed, 'w', encoding='utf8') as outfile:
            print(r_text, file=outfile)
        return False

    data = r_text.split('¬')

    data_list = [{}]

    for item in data:
        key = item.split('÷')[0]
        value = item.split('÷')[-1]
        value = checkdate(value)

        if '~' in key:
            data_list.append({key: value})
        else:
            data_list[-1].update({key: value})

    # for game in data_list:
        # print(game)
        # if 'AA' in list(game.keys())[0]:
        #     date = datetime.fromtimestamp(int(game.get("AD")))
        #     team_1 = game.get("AE")
        #     team_2 = game.get("AF")
        #     score = f'{game.get("AG")} : {game.get("AH")}'

        #     print(date, team_1, team_2, score, sep='/')

    with open(feed+'.json', 'w', encoding='utf8') as outfile:
        json.dump(data_list, outfile, ensure_ascii=False, indent=2)
    return data_list

def checkdate(value):
    if len(value)==10 and value.isdigit():
        if int(value)>1234567890:
            value = str(datetime.fromtimestamp(int(value)))
    return value

def GetSportGames(sport):
    global feed
    feed = f'f_{sport}_0_3_ru_1'
    # url_g = f'https://2.flashscore.ninja/802/x/feed/{feed}'

    response = requests.get(url=url+feed, headers=headers)
    r_text = response.text
    if is_data(r_text):
        games = prepars(r_text)
    return games

def GetGameData(game, data_type):

    if data_type == 'summary':
        d_feed = 'df_sui_1_'
    elif data_type == 'stats':
        d_feed = 'df_st_1_'
    elif data_type == 'commentary':
        d_feed = 'df_lc_1_'
    elif data_type == 'odds':
        d_feed = 'df_od_1_'
    elif data_type == 'h2h':
        d_feed = 'df_hh_1_'
    else:
        d_feed = 'dc_1_'


    global feed
    # feed = f'dc_1_{game}'
    # feed = f'df_hh_3_{game}'
    feed = d_feed+game
   # url = f'https://2.flashscore.ninja/802/x/feed/{feed}'

    response = requests.get(url=url+feed, headers=headers)
    r_text = response.text
    if is_data(r_text):
        games = prepars(r_text)
    return games


if __name__ == '__main__':
    main()