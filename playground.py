from flask import Flask, jsonify, request
import requests
from src.models.players import Players
from src.team_id_finder import team_finder

app = Flask(__name__)
players = []


# [GET] Jugadores por equipo y temporada

@app.route('/api/NBA/players', methods=['GET'])
def get_player():
    season = request.args.get('season')
    team = team_finder(request.args.get('search'))

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
                players.append(
                    Players(
                        player_dict['id'],
                        player_dict['firstname'],
                        player_dict['lastname'],
                        player_dict['birth']['date'],
                        player_dict['birth']['country'],
                        player_dict['nba']['pro'],
                        player_dict['height']['meters'],
                        player_dict['weight']['kilograms']
                    )
                )
            except TypeError:
                continue

    for player in players:
        return jsonify({'players': player.serialize(), 'status': 'ok'})
