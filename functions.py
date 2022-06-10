def welcome():
    print('\t\t*********************************')
    print('\t\t* Welcome to your player finder *')
    print('\t\t*********************************')


def user_menu():
    print('---------------------'
          'Main menu:'
          '\t(1) Find a player by its attributes and stats'
          '\t(2) Find player stats by team'
          '\t(3) Quit'
          '---------------------')


def team_finder(team_name):
    import requests
    search = team_name
    response = requests.get(
        "https://api-nba-v1.p.rapidapi.com/teams?",
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        },
        params={'search': search}
    )
    status_code = response.status_code
    if status_code == 200:
        json = response.json()
        for team in json['response']:
            return team['id']
    else:
        print('Error')


def team_id_finder(id):
    import requests
    response = requests.get(
        "https://api-nba-v1.p.rapidapi.com/teams?id=" + id,
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )
    status_code = response.status_code
    if status_code == 200:
        json = response.json()
        for team in json['response']:
            name = team["name"]
            return f'\nOk lets find you a player from the {name.upper()}'
    else:
        print('Error')


def player_position_finder(player_id):
    import requests
    response = requests.get(
        "https://api-nba-v1.p.rapidapi.com/player/statistics?season=2020&id=" + player_id,
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )

    status_code = response.status_code

    if status_code == 200:
        json = response.json()
        # print(json['response']) -- permite ver todos los atributos
        for player in json['response']:
            return player['pos']
    else:
        print('Error')


def player_stats(team, firstname, lastname):
    import statistics
    import requests

    response = requests.get(
        "https://api-nba-v1.p.rapidapi.com/players/statistics?season=2020&team=" + team,
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )
    status_code = response.status_code

    games_counter = 0
    fgp_per_game = []
    tpp_per_game = []
    points_per_game = []
    assists_per_game = []
    rebounds_per_game = []
    blocks_per_game = []
    steals_per_game = []
    turnovers_per_game = []

    if status_code == 200:
        json = response.json()
        for dict in json['response']:
            try:
                if (dict['player']['firstname'] == firstname and dict['player']['lastname']) == lastname:
                    games_counter += 1
                    fgp_per_game.append(float(dict['fgp']))
                    tpp_per_game.append(float(dict['tpp']))
                    points_per_game.append(dict['points'])
                    assists_per_game.append(dict['assists'])
                    rebounds_per_game.append(dict['totReb'])
                    steals_per_game.append(dict['steals'])
                    blocks_per_game.append(dict['blocks'])
                    turnovers_per_game.append(dict['turnovers'])
            except TypeError:
                continue

        if games_counter == 0:
            print('We could not find your player, please try another one.')

        else:
            stats = {'name': f'{firstname} {lastname}',
                     'fg%': round(statistics.mean(fgp_per_game), 2),
                     '3p%': round(statistics.mean(tpp_per_game), 2),
                     'points': round(statistics.mean(points_per_game)),
                     'assists': round(statistics.mean(assists_per_game)),
                     'rebounds': round(statistics.mean(rebounds_per_game)),
                     'steals': round(statistics.mean(steals_per_game)),
                     'blocks': round(statistics.mean(blocks_per_game)),
                     'turnovers': round(statistics.mean(turnovers_per_game))
                     }

            return stats


def print_stats(player):
    for k, v in player.items():
        if k == 'name':
            print(f'\n{v.upper()}')
        elif k == 'fg%':
            print(f'\tField goal %: {v}')
        elif k == '3p%':
            print(f'\tThree point %: {v}')
        else:
            print(f'\t{k.title()}: {v}')


def teams_list():
    import requests
    response = requests.get(
        "https://api-nba-v1.p.rapidapi.com/teams?",
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )
    status_code = response.status_code
    teams = []
    if status_code == 200:
        json = response.json()
        for team in json['response']:
            if team['nbaFranchise']:
                teams.append(str(team['id']))
            else:
                continue
        return teams
    else:
        return 'Error'





