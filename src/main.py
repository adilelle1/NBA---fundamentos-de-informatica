from flask import Flask, jsonify, request
import requests
import statistics
from src.models.players import Players
from src.functions import team_finder
from src.models.teams import Teams

app = Flask(__name__)


#
# [GET] Estadistica de equipo por temporada

@app.route('/teams', methods=['GET'])
def team_finder():
    search = request.args.get("search")
    season = request.args.get('season')

    response1 = requests.get(
        "https://api-nba-v1.p.rapidapi.com/teams?search=" + search,
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )
    status_code = response1.status_code
    if status_code == 200:
        json1 = response1.json()
        for team in json1["response"]:
            for key, value in team.items():
                if key == 'id':
                    team_id = str(value)
                elif key == 'name':
                    team_name = value
                elif key == 'city':
                    team_city = value

    response2 = requests.get(
        "https://api-nba-v1.p.rapidapi.com/teams/statistics?season=" + str(season) + "&id=" + str(team_id),
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        }
    )
    status_code = response2.status_code
    if status_code == 200:
        json2 = response2.json()
        for team in json2["response"]:
            for key, value in team.items():
                if key == 'games':
                    games = value
                elif key == 'points':
                    points = round(value / games, 2)
                elif key == 'totReb':
                    rebounds = round(value / games, 2)
                elif key == 'assists':
                    assists = round(value / games, 2)
    team = Teams(team_id, team_name, team_city, season, games, points, rebounds, assists)
    return jsonify({'team': team.__dict__, 'status': 'ok'})


#
# [GET] Estadísticas de jugadores por equipo y temporada

@app.route('/players', methods=['GET'])
def player_finder():
    searched_players = []
    season = request.args.get('season')
    team = team_finder(request.args.get('search'))
    fgp_per_game = []
    tpp_per_game = []
    points_per_game = []
    assists_per_game = []
    rebounds_per_game = []
    blocks_per_game = []
    steals_per_game = []
    turnovers_per_game = []

    http_rsp_player = requests.get(
        "https://api-nba-v1.p.rapidapi.com/players?season=" + str(season) + "&team=" + str(team),
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "1e5e5821femsh450b4f3086376a6p114414jsne8cc7f313f90"
        })
    status_code_2 = http_rsp_player.status_code

    if status_code_2 == 200:
        json = http_rsp_player.json()
        for player_dict in json['response']:
            try:
                firstname = player_dict['firstname']
                lastname = player_dict['lastname']
                birth = player_dict['birth']['date']
                country = player_dict['birth']['country']
                pro_years = player_dict['nba']['pro']
                height = player_dict['height']['meters']
                weight = player_dict['weight']['kilograms']

                http_rsp_stats = requests.get(
                    "https://api-nba-v1.p.rapidapi.com/players/statistics?season=" + str(season) + "&team=" + str(team),
                    headers={
                        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
                        'x-rapidapi-key': "74cff2d19bmshc82b77265cf59c6p179774jsnc9d690a6ad65"
                    })
                status_code_1 = http_rsp_stats.status_code

                if status_code_1 == 200:
                    json = http_rsp_stats.json()
                    for stast_dict in json['response']:
                        if firstname == stast_dict['player']['firstname'] \
                                and lastname == stast_dict['player']['lastname']:
                            fgp_per_game.append(float(stast_dict['fgp']))
                            tpp_per_game.append(float(stast_dict['tpp']))
                            points_per_game.append(stast_dict['points'])
                            assists_per_game.append(stast_dict['assists'])
                            rebounds_per_game.append(stast_dict['totReb'])
                            steals_per_game.append(stast_dict['steals'])
                            blocks_per_game.append(stast_dict['blocks'])
                            turnovers_per_game.append(stast_dict['turnovers'])
                            try:
                                team = stast_dict['team']['name']
                                if stast_dict['pos']:
                                    position = stast_dict['pos']
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
                my_player = Players(firstname, lastname, birth, country, pro_years, height, weight, team, season,
                                    position, points, fg_percentage, tp_percentage, rebounds, assists, steals,
                                    turnovers,
                                    blocks)
                searched_players.append(my_player)
            except TypeError:
                continue

    for player in searched_players:
        return jsonify({'players': player.__dict__, 'status': 'ok'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
