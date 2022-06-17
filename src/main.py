import statistics
from flask import Flask, jsonify, request
import requests

from src.db.client_store import store_client_file
from src.models.players import Players, PlayerStats
from src.team_id_finder import team_finder
from src.models.teams import Teams
from src.models.clients import Client
from db.client_loader import load_clients

app = Flask(__name__)
clients = load_clients()
players = []


#
# [GET] Estadística de equipo por temporada

@app.route('/api/NBA/teams', methods=['GET'])
def get_team():
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
    return jsonify({'team': team.serialize(), 'status': 'ok'})


#
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


#
# [GET] Estadísticas de jugadores por equipo y temporada

@app.route('/api/NBA/players/stats', methods=['GET'])
def get_player_stats():
    season = request.args.get('season')
    player_id = request.args.get('id')
    fgp_per_game = []
    tpp_per_game = []
    points_per_game = []
    assists_per_game = []
    rebounds_per_game = []
    blocks_per_game = []
    steals_per_game = []
    turnovers_per_game = []

    http_rsp_stats = requests.get(
        "https://api-nba-v1.p.rapidapi.com/players/statistics?season=" + str(season) + "&id=" + str(player_id),
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

        return jsonify({'players': player_stats.serialize(), 'status': 'ok'})


#
# [GET] Todos los clientes

@app.route("/api/NBA/clients/", methods=['GET'])
def get_all_clients():
    return jsonify({'players': [cli.serialize() for cli in clients], 'status': 'ok'})


#
# [GET] Clientes por id

@app.route("/api/NBA/clients/<clients_id>", methods=['GET'])
def get_client(clients_id):
    for client in clients:
        if client.client_id == clients_id:
            return jsonify({'players': client.serialize(), 'status': 'ok'})

    return jsonify({})


#
# [POST] Crear clientes

@app.route("/api/NBA/clients/", methods=['POST'])
def create_client():
    client = request.json

    try:
        new_client = Client(
            client['client_id'],
            client['first_name'],
            client['last_name'],
            client['date_of_birth'],
            client['email'],
            client['client_status'],
            client['category'],
            client['subscription_info']
        )

        clients.append(new_client)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code=400,
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(new_client.serialize())


#
# [PUT] Actualizar la categoria del cliente

@app.route("/api/NBA/clients/category", methods=['PUT'])
def upgrade_client_category():
    client_id = request.args.get('client_id')
    new_category = request.args.get('new_category')
    try:
        for client in clients:
            if client['client_id'] == client_id:
                upgraded_client = Client.category_upgrade(client, new_category)

        clients.append(upgraded_client)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code=400,
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(upgraded_client.__dict__)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
