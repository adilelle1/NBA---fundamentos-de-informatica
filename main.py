import requests

from functions import welcome, team_finder, player_stats, print_stats

while True:
    welcome()
    team = str(team_finder())

    # defino lista vacia para appendear diccionarios con las stats de los jugadores que cumplen los filtros ------------
    searched_players_stats = []

    # attributes --------------------------------------------------------------------------------------
    print('\nInsert your player attributes:')
    position = input('\tPosition (B/SG/SF/PF/C):')
    # print('\tAge')
    # min_age = int(input('\t\tMinimum age:'))
    # max_age = int(input('\t\tMaximum age:'))
    print('\tHeight in meters (ex 1.9)')
    min_height = float(input('\t\tMinimum height:'))
    max_height = float(input('\t\tMaximum height:'))
    print('\tWeight in kilograms (ex 110.5)')
    min_weight = float(input('\t\tMinimum weight:'))
    max_weight = float(input('\t\tMaximum weight:'))

    # stats ----------------------------------------
    print('\nInsert your player stats:')
    min_fgp = float(input('\t\tMinimum field goal % (ex 30.5):'))
    min_tpp = float(input('\t\tMinimum three point % (ex 30.5):'))
    min_points = int(input('\t\tMinimum points:'))
    min_rebounds = int(input('\t\tMinimum rebounds:'))
    min_assists = int(input('\t\tMinimum assists:'))
    min_steals = int(input('\t\tMinimum steals:'))
    min_turnovers = int(input('\t\tMaximum turnovers:'))
    min_blocks = int(input('\t\tMinimum blocks:'))

    # buscamos los jugadores que cumplan con los filtros de atributos y los appendeamos a una lista de diccionarios
    # calculando para cada uno el promedio por temporada de sus estadísticas usando la funcion player_stats
    # esto se hace sobre el endpoint de players que trae datos del jugador, no estadísticas
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
        for player_dict in json['response']:
            try:
                if min_weight <= float(player_dict['weight']['kilograms']) <= max_weight \
                        and min_height <= float(player_dict['height']['meters']) <= max_height:
                    firstname = player_dict['firstname']
                    lastname = player_dict['lastname']
                    # llamo la funcion que usa el endpoint de players/statistics y devuelve un diccionario con los
                    # promedios del jugador
                    searched_players_stats.append(player_stats(team, firstname, lastname))

            except TypeError:
                continue

        if not searched_players_stats:
            print('\nWe are sorry, no players match your request.')
            break

    else:
        print('Error')

    # de la lista de diccionarios que creamos buscamos cada estadistica de cada jugador y la igualamos a los filtros
    # que ingreso el usuario para printear solo aquellos que cumplan con dichas condiciones

    for player in searched_players_stats:
        if player['fg%'] >= min_fgp \
                and player['3p%'] >= min_tpp \
                and player['points'] >= min_points \
                and player['assists'] >= min_assists \
                and player['rebounds'] >= min_rebounds \
                and player['steals'] >= min_steals \
                and player['turnovers'] <= min_turnovers \
                and player['blocks'] >= min_blocks:
            print('\nThese players match your request:')
            print(print_stats(player))
