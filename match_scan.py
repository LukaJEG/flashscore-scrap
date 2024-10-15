import configparser
import flashscore

def GetSport():
    sports = {'1': 'Futball', '2': 'Tennis'}

    print('Выберите вид спорта из перечня:')
    for key, value in sports.items():
        print(f"{key}: {value}")

    sport = input("Введите нужную цифру: ")
    if not(sport in sports):
       print(f"Неверный вид спорта")
       sport = '0'
    return sport

def GetGame():
    game = input("Введите игру: ")
    return game


def main():
    # sport=GetSport()
    sport = '1'
    print(sport)
    if sport == '0':
        return False
    # game=GetGame()
    game = 'bn'
    print(game)
    if game is None:
        return False

    games = flashscore.GetSportGames(sport)
    # print(games)

    game = flashscore.GetGameData("rexZDSJT")
    print(game)


if __name__ == '__main__':
    main()
