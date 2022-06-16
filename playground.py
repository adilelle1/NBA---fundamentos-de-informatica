import requests
import statistics
from src.models.players import PlayerStats

season = 2020
id = 75
player_stats_list = []
fgp_per_game = []
tpp_per_game = []
points_per_game = []
assists_per_game = []
rebounds_per_game = []
blocks_per_game = []
steals_per_game = []
turnovers_per_game = []

http_rsp_stats = requests.get(
    "https://api-nba-v1.p.rapidapi.com/players/statistics?season=" + str(season) + "&id=" + str(id),
    headers={
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': "74cff2d19bmshc82b77265cf59c6p179774jsnc9d690a6ad65"
    })
status_code_1 = http_rsp_stats.status_code

if status_code_1 == 200:
    json = http_rsp_stats.json()
    for stats_dict in json['response']:
        try:
            fgp_per_game.append(float(stats_dict['fgp']))
            tpp_per_game.append(float(stats_dict['tpp']))
            points_per_game.append(stats_dict['points'])
            assists_per_game.append(stats_dict['assists'])
            rebounds_per_game.append(stats_dict['totReb'])
            steals_per_game.append(stats_dict['steals'])
            blocks_per_game.append(stats_dict['blocks'])
            turnovers_per_game.append(stats_dict['turnovers'])

            player_firstname = stats_dict['player']['firstname']
            player_lastname = stats_dict['player']['lastname']

            team = stats_dict['team']['name']
            if stats_dict['pos']:
                position = stats_dict['pos']
            else:
                position = None
        except TypeError:
            continue

    points = round(statistics.mean(points_per_game))
    fg_percentage = round(statistics.mean(fgp_per_game), 2)
    tp_percentage = round(statistics.mean(tpp_per_game), 2)
    assists = round(statistics.mean(assists_per_game))
    rebounds = round(statistics.mean(rebounds_per_game))
    steals = round(statistics.mean(steals_per_game))
    blocks = round(statistics.mean(blocks_per_game))
    turnovers = round(statistics.mean(turnovers_per_game))

    player_stats = PlayerStats(player_firstname, player_lastname, team, season, position, points, fg_percentage,
                               tp_percentage, rebounds, assists, steals, turnovers, blocks)
    print(player_stats.serialize())

