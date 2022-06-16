class Client:
    def __init__(self, client_id, firstname, lastname, date_of_birth, email,client_status,category, subscription_info):
        self.client_id = client_id
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.email = email
        self.client_status = client_status
        self.category = category
        self.subscription = subscription_info

    def __str__(self) -> str:
        return super().__str__()

    def category_upgrade(self, new_category):
        if new_category == "Rookie" or new_category == "rookie":
            client = Rookie(self.client_id, self.firstname, self.lastname, self.date_of_birth, self.email,
                            self.client_status, new_category, self.subscription)
        elif new_category == "All star" or new_category == "all star" or new_category == "All Star":
            client = AllStar(self.client_id, self.firstname, self.lastname, self.date_of_birth, self.email,
                             self.client_status, new_category, self.subscription)
        elif new_category == "Hall of fame" or new_category == "hall of fame":
            client = HallOfFame(self.client_id, self.firstname, self.lastname, self.date_of_birth, self.email,
                                self.client_status, self.subscription)

    def serialize(self):
        return {
            'client_id': self.client_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'date_of_birth': self.date_of_birth,
            'email': self.email,
            'client_status': self.client_status,
            'category': self.category,
            'subscription': self.subscription
        }


class Rookie(Client):
    def __init__(self, client_id, firstname, lastname, date_of_birth, email, client_status, category,
                 subscription_info):
        super().__init__(client_id, firstname, lastname, date_of_birth, email, client_status, category,
                         subscription_info)
        self.category = "Rookie"
        self.benefits = ["5 requests per hour", "1 power search per month", "1 tailor-made advice per year"]


class AllStar(Client):
    def __init__(self, client_id, firstname, lastname, date_of_birth, email, client_status, category,
                 subscription_info):
        super().__init__(client_id, firstname, lastname, date_of_birth, email, client_status, category,
                         subscription_info)
        self.category = "All Star"
        self.benefits = ["25 requests per hour", "5 power search per month", "12 tailor-made advice per year"]


class HallOfFame(Client):
    def __init__(self, client_id, firstname, lastname, date_of_birth, email, client_status, category,
                 subscription_info):
        super().__init__(client_id, firstname, lastname, date_of_birth, email, client_status, category,
                         subscription_info)
        self.category = "Hall of Fame"
        self.benefits = ["unlimited requests per hour", "unlimited power search per month",
                         "unlimited tailor-made advice per year"]

