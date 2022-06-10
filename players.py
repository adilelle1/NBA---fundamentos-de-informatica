class Players:

    def __init__(self, firstname, lastname, birth, country, pro_years, height, weight, team, season, position,
                 points, field_goal_percentage, three_point_percentage, rebounds, assists, steals, turnovers, blocks):
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth
        self.country = country
        self.pro_years = pro_years
        self.height = height
        self.weight = weight
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
        return f'Name: {self.firstname}, {self.lastname}' \
               f'\n\tBirth: {self.birth}' \
               f'\n\tCountry: {self.country}' \
               f'\n\tHeight: {self.height}' \
               f'\n\tWeight: {self.weight}' \
               f'\n\tPro years: {self.pro_years}' \
               f'\n\tTeam: {self.team}'



