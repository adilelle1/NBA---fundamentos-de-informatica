import requests

from functions import welcome, player_stats, teams_list, print_stats

while True:
    welcome()

    # defino lista vacia para appendear diccionarios con las stats de los jugadores que cumplieron -----------------
    searched_players_stats = []

    # buscar usando atributos --------------------------------------------------------------------------------------
    print('\nInsert your player attributes:')
    position = input('\tPosition(B/SG/SF/PF/C)>> ')
    # print('\tAge')
    # min_age = int(input('\t\tMinimum age:'))
    # max_age = int(input('\t\tMaximum age:'))
    print('\tHeight in meters (ex: 1.9)')
    min_height = float(input('\t\tMinimum height >>'))
    max_height = float(input('\t\tMaximum height >> '))
    print('\tWeight in kilograms (ex: 110.5)')
    min_weight = float(input('\t\tMinimum weight >> '))
    max_weight = float(input('\t\tMaximum weight >> '))

    print('\nInsert your player stats:')
    min_fgp = float(input('\t\tMinimum field goal percentage(ex 30.5) >> '))
    min_tpp = float(input('\t\tMinimum 3 point percentage(ex 30.5) >> '))
    min_points = int(input('\t\tMinimum points >> '))
    # min_rebounds = int(input('\t\tMinimum rebounds >> '))
    # min_assists = int(input('\t\tMinimum assists >> '))
    # min_steals = int(input('\t\tMinimum steals >> '))
    # min_turnovers = int(input('\t\tMaximum turnovers >> '))
    # min_blocks = int(input('\t\tMinimum blocks >> '))

    teams = teams_list()

    for team in teams:

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
            for dict in json['response']:
                try:
                    if min_weight <= float(dict['weight']['kilograms']) <= max_weight \
                            and min_height <= float(dict['height']['meters']) <= max_height:
                        firstname = dict['firstname']
                        lastname = dict['lastname']
                        # llamo la funcion que me devuelve un diccionario con los promedios del jugador
                        searched_players_stats.append(player_stats(team, firstname, lastname))

                except TypeError:
                    continue
                except AttributeError:
                    continue

            if not searched_players_stats:
                print('\nWe are sorry, no players match your request.')
                break

        else:
            continue

        # stats ----------------------------------------

    for player in searched_players_stats:
        try:

            if player['fg%'] >= min_fgp \
                    and player['3p%'] >= min_tpp \
                    and player['points'] >= min_points:
                # and player['assists'] >= min_assists \
                # and player['rebounds'] >= min_rebounds \
                # and player['steals'] >= min_steals \
                # and player['turnovers'] <= min_turnovers \
                # and player['blocks'] >= min_blocks:
                print(print_stats(player))
        except TypeError:
            continue

