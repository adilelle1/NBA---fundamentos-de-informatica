def welcome():
    print('*********************************')
    print('* Welcome to your player finder *')
    print('*********************************')


def user_menu():
    print('---------------------'
          'Main menu:'
          '\t(1) Find using attributes'
          '\t(2) Find using game stats'
          '\t(3) Quit'
          '' - --------------------'')


def team_finder():
    import requests
    team = input("\nInsert your team's name>>")

    response = requests.get(
        "https://api-nba-v1.p.rapidapi.com/teams?search=" + team,
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )

    status_code = response.status_code

    if status_code == 200:
        json = response.json()
        # print(json['response']) -- permite ver todos los atributos
        for team in json['response']:
            return team['id']
    else:
        print('Error')
