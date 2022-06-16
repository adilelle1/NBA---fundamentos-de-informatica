class Players:

    def __init__(self, player_id, firstname, lastname, birth, country, pro_years, height, weight):
        self.player_id = player_id
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth
        self.country = country
        self.pro_years = pro_years
        self.height = height
        self.weight = weight

    def __str__(self) -> str:
        return super().__str__()

    def serialize(self):
        return {
            'player_id': self.player_id,
            'first_name': self.firstname,
            'last_name': self.lastname,
            'birth': self.birth,
            'country': self.pro_years,
            'height': self.height,
            'weight': self.weight
        }


class PlayerStats:
    def __init__(self, firstname, lastname, team, season, position, points, field_goal_percentage,
                 three_point_percentage, rebounds, assists, steals, turnovers, blocks):
        self.firstname = firstname
        self.lastname = lastname
        self.team = team
        self.season = season
        self.position = position
        self.points = points
        self.field_goal_percentage = field_goal_percentage
        self.three_point_percentage = three_point_percentage
        self.rebounds = rebounds
        self.assists = assists
        self.steals = steals
        self.turnovers = turnovers
        self.blocks = blocks

    def __str__(self) -> str:
        return super().__str__()

    def serialize(self):
        return {
            'first_name': self.firstname,
            'last_name': self.lastname,
            'team': self.team,
            'season': self.season,
            'position': self.position,
            'points': self.points,
            'fg_percentage': self.field_goal_percentage,
            'tp_percentage': self.three_point_percentage,
            'rebounds': self.rebounds,
            'assists': self.assists,
            'steals': self.steals,
            'turnovers': self.turnovers,
            'blocks': self.blocks
        }
