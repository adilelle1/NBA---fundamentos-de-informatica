class Client:
    def __init__(self, client_id, firstname, lastname, date_of_birth, email, subscription_info, client_status,
                 category):
        self.client_id = client_id
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.email = email
        self.subscription = subscription_info
        self.client_status = client_status
        self.category = category

    def __str__(self) -> str:
        return super().__str__()

    def category_upgrade(self, new_category):
        if new_category == "Rookie" or new_category == "rookie":
            client = Rookie(self.client_id, self.firstname, self.lastname, self.date_of_birth, self.email,
                            self.subscription, self.client_status)
        elif new_category == "All star" or new_category == "all star" or new_category == "All Star":
            client = AllStar(self.client_id, self.firstname, self.lastname, self.date_of_birth, self.email,
                             self.subscription, self.client_status)
        elif new_category == "Hall of fame" or new_category == "hall of fame":
            client = HallOfFame(self.client_id, self.firstname, self.lastname, self.date_of_birth, self.email,
                                self.subscription, self.client_status)


class Rookie(Client):
    def __init__(self, client_id, firstname, lastname, date_of_birth, email, subscription_info, client_status,
                 category):
        super().__init__(client_id, firstname, lastname, date_of_birth, email, subscription_info, client_status,
                         category)
        self.category = "Rookie"
        self.benefits = ["5 requests per hour", "1 power search per month", "1 tailor-made advice per year"]


class AllStar(Client):
    def __init__(self, client_id, firstname, lastname, date_of_birth, email, subscription_info, client_status,
                 category):
        super().__init__(client_id, firstname, lastname, date_of_birth, email, subscription_info, client_status,
                         category)
        self.category = "All Star"
        self.benefits = ["25 requests per hour", "5 power search per month", "12 tailor-made advice per year"]


class HallOfFame(Client):
    def __init__(self, client_id, firstname, lastname, date_of_birth, email, subscription_info, client_status,
                 category):
        super().__init__(client_id, firstname, lastname, date_of_birth, email, subscription_info, client_status,
                         category)
        self.category = "Hall of Fame"
        self.benefits = ["unlimited requests per hour", "unlimited power search per month",
                         "unlimited tailor-made advice per year"]


class Subscription:
    def __init__(self, type, start_date, expiry_date, active):
        self.type = type
        self.start_date = start_date
        self.expiry_date = expiry_date
        self.active = active

    def __str__(self) -> str:
        return super().__str__()
