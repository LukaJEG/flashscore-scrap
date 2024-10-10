import json
import requests
from datetime import datetime


headers = {"x-fsign": "SW9D1eZo"}


def main():
    feed = 'f_1_-1_3_ru_5'
    url = f'https://d.flashscore.ru.com/x/feed/{feed}'
    response = requests.get(url=url, headers=headers)
    data = response.text.split('¬')

    data_list = [{}]

    for item in data:
        key = item.split('÷')[0]
        value = item.split('÷')[-1]

        if '~' in key:
            data_list.append({key: value})
        else:
            data_list[-1].update({key: value})

    for game in data_list:
        if 'AA' in list(game.keys())[0]:
            date = datetime.fromtimestamp(int(game.get("AD")))
            team_1 = game.get("AE")
            team_2 = game.get("AF")
            score = f'{game.get("AG")} : {game.get("AH")}'

            print(date, team_1, team_2, score, sep='/')

            # print(json.dumps(game, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()