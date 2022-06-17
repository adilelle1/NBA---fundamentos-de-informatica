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

