import numpy as np
import requests

from teams import welcome, team_finder

while True:
    welcome()
    team = str(team_finder())

    searched_players = []
    searched_players_unique = []

    # buscar usando atributos --------------------------------------------------------------------------------------

    print('\nInsert your player attributes:')
    position = input('\tPosition (B/SG/SF/PF/C):')
    # age = int(input('\tAge:'))  # hacer la diferencia entre todays date y dict['birth']['date'], todavia no lo pude resolver
    # years_pro = int(input('\tPro years:'))  # dict['nba']['pro']
    height = float(input('\tHeight in meters (ex: 1.9):'))
    weight = float(input('\tWeight in kilograms (ex: 110.5):'))

    response = requests.get(
        "https://api-nba-v1.p.rapidapi.com/players?season=2020&team=" + team,
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )
    status_code = response.status_code

    if status_code == 200:
        json = response.json()
        # response es una key del json, su value es una lista de diccionarios
        for dict in json['response']:
            try:
                if float(dict['height']['meters']) >= height \
                        and float(dict['weight']['kilograms']) >= weight:
                    # and (today - dict['birth']['age']) >= age \

                    searched_players.append(dict['firstname'] + ' ' + dict['lastname'])
            except TypeError:
                continue

        if not searched_players:
            print('\nWe are sorry, no players match your request.')
        else:
            print('\nThese players match your request:')
            for player in np.unique(searched_players):
                searched_players_unique.append(player)

    else:
        print('Error')

    # stats ----------------------------------------

    print('\nInsert your player stats:')
    fgp = float(input('\tField goal percentage(ex 30.5):'))
    tpp = float(input('\tThree point percentage(ex 3.5):'))
    points = int(input('\tPoints:'))
    rebounds = int(input('\tRebounds:'))
    assists = int(input('\tAssists:'))
    steals = int(input('\tSteals:'))
    turnovers = int(input('\tTurnovers:'))
    blocks = int(input('\tBlocks:'))
    plus_minus = int(input('\tPlus/Minus +/-:'))

    response = requests.get(
        "https://api-nba-v1.p.rapidapi.com/players/statistics?season=2020&team=" + team,
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )
    status_code = response.status_code

    if status_code == 200:
        json = response.json()
        for dict in json['response']:
            try:
                if (dict['player']['firstname'] + ' ' + dict['player']['lastname']) in searched_players_unique \
                        and dict['pos'] == position \
                        and float(dict['fgp']) >= fgp \
                        and float(dict['tpp']) >= tpp \
                        and dict['points'] >= points \
                        and dict['assists'] >= assists \
                        and dict['totReb'] >= rebounds \
                        and dict['steals'] >= steals \
                        and dict['turnovers'] >= turnovers \
                        and dict['blocks'] >= blocks \
                        and float(dict['plusMinus']) >= plus_minus:
                    searched_players.append(dict['player']['firstname'] + ' ' + dict['player']['lastname'])

            except TypeError:
                continue

        if not searched_players:
            print('\nWe are sorry, no players match your request.')
        else:
            print('\nThese players match your request:')

            for player in np.unique(searched_players):
                print(f'\t{player}')

        # response es una key del json, su value es una lista de diccionarios
    else:
        print('Error')
