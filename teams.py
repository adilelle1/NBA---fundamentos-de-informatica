class Teams:

    def __init__(self, team_id, name, city, season, games, points, rebounds, assists):
        self.team_id = team_id
        self.name = name
        self.city = city
        self.season = season
        self.games = games
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def __str__(self) -> str:
        return super().__str__()


