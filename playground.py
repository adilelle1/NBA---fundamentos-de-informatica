from flask import Flask, jsonify, request
import requests
import statistics
from src.models.players import Players
from src.functions import team_finder

searched_players = []
counter = 0
my_players = {}
season = '2020'
team = str(team_finder('golden'))
fgp_per_game = []
tpp_per_game = []
points_per_game = []
assists_per_game = []
rebounds_per_game = []
blocks_per_game = []
steals_per_game = []
turnovers_per_game = []

http_rsp_player = requests.get("https://api-nba-v1.p.rapidapi.com/players?season=" + season + "&team=" + team,
                               headers={
                                   'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
                                   'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
                               })
status_code_2 = http_rsp_player.status_code

if status_code_2 == 200:
    json = http_rsp_player.json()
    for player_dict in json['response']:
            try:
                if int(player_dict['height']['meters']) >= 1.9 and int(player_dict['weight']['kilograms']) >= 90:
                    firstname = player_dict['firstname']
                    lastname = player_dict['lastname']
                    birth = player_dict['birth']['date']
                    country = player_dict['birth']['country']
                    pro_years = player_dict['nba']['pro']
                    height = player_dict['height']['meters']
                    weight = player_dict['weight']['kilograms']

                    http_rsp_stats = requests.get(
                        "https://api-nba-v1.p.rapidapi.com/players/statistics?season=2020&team=" + team,
                        headers={
                            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
                            'x-rapidapi-key': "74cff2d19bmshc82b77265cf59c6p179774jsnc9d690a6ad65"
                        })
                    status_code_1 = http_rsp_stats.status_code

                    if status_code_1 == 200:
                        json = http_rsp_stats.json()
                        for player_dict in json['response']:
                            if firstname == player_dict['player']['firstname'] \
                                    and lastname == player_dict['player']['lastname']:
                                counter += 1
                                fgp_per_game.append(float(player_dict['fgp']))
                                tpp_per_game.append(float(player_dict['tpp']))
                                points_per_game.append(player_dict['points'])
                                assists_per_game.append(player_dict['assists'])
                                rebounds_per_game.append(player_dict['totReb'])
                                steals_per_game.append(player_dict['steals'])
                                blocks_per_game.append(player_dict['blocks'])
                                turnovers_per_game.append(player_dict['turnovers'])
                                try:
                                    team = player_dict['team']['name']
                                    if player_dict['pos']:
                                        position = player_dict['pos']
                                    else:
                                        position = None
                                    points = round(statistics.mean(points_per_game))
                                    fg_percentage = round(statistics.mean(fgp_per_game), 2)
                                    tp_percentage = round(statistics.mean(tpp_per_game), 2)
                                    assists = round(statistics.mean(assists_per_game))
                                    rebounds = round(statistics.mean(rebounds_per_game))
                                    steals = round(statistics.mean(steals_per_game))
                                    blocks = round(statistics.mean(blocks_per_game))
                                    turnovers = round(statistics.mean(turnovers_per_game))

                                except TypeError:
                                    continue

            except TypeError:
                continue
            except ValueError:
                continue
            my_player = Players(firstname, lastname, birth, country, pro_years, height, weight, team, season, position,
                                points, fg_percentage, tp_percentage, rebounds, assists, steals, turnovers, blocks)
            searched_players.append(my_player)

for player in searched_players:
    print(player.__dict__)