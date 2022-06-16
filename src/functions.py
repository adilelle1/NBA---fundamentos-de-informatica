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


def create_player_stats(players_list, season, team):
    import requests
    import statistics
    from src.models.players import PlayerStats

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
        "https://api-nba-v1.p.rapidapi.com/players/statistics?season=" + str(season) + "&team=" + str(team),
        headers={
            'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
            'x-rapidapi-key': "74cff2d19bmshc82b77265cf59c6p179774jsnc9d690a6ad65"
        })
    status_code_1 = http_rsp_stats.status_code

    if status_code_1 == 200:
        json = http_rsp_stats.json()
        for ply in players_list:
            for stats_dict in json['response']:
                if ply['firstname'] == stats_dict['player']['firstname'] \
                        and ply['lastname'] == stats_dict['player']['lastname']:
                    try:
                        fgp_per_game.append(float(stats_dict['fgp']))
                        tpp_per_game.append(float(stats_dict['tpp']))
                        points_per_game.append(stats_dict['points'])
                        assists_per_game.append(stats_dict['assists'])
                        rebounds_per_game.append(stats_dict['totReb'])
                        steals_per_game.append(stats_dict['steals'])
                        blocks_per_game.append(stats_dict['blocks'])
                        turnovers_per_game.append(stats_dict['turnovers'])
                    except TypeError:
                        continue

                    try:
                        if stats_dict['pos']:
                            position = stats_dict['pos']
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

                        player_stats = PlayerStats(ply['firstname'], ply['lastname'], ply['birth'], ply['country'],
                                                   ply['pro_years'], ply['height'], ply['weight'],
                                                   stats_dict['team']['name'], season, position, points, fg_percentage,
                                                   tp_percentage, rebounds, assists, steals, turnovers, blocks)
                        player_stats_list.append(player_stats)
                    except TypeError:
                        continue
    return player_stats_list
