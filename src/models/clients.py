class Client:
    def __init__(self, client_id, firstname, lastname, subscription_info, client_status):
        self.client_id = client_id
        self.firstname = firstname
        self.lastname = lastname
        self.subscription = subscription_info
        self.client_status = client_status


class Rookie(Client):
    def __init__(self, client_id, firstname, lastname, subscription_info, client_status):
        super().__init__(client_id, firstname, lastname, subscription_info, client_status)
        self.category = "Rookie client"
        self.benefits = ["5 requests per hour", "1 power search per month", "1 tailor-made advice per year"]

    def category_upgrade(self):
        from flask import request
        new_category = request.args.get("search")
        if new_category == "All star" or new_category == "all star" or new_category == "All Star":
            client = AllStar(self.client_id, self.firstname, self.lastname, self.subscription, self.client_status)
        elif new_category == "Hall of fame" or new_category == "hall of fame":
            client = AllStar(self.client_id, self.firstname, self.lastname, self.subscription, self.client_status)


class AllStar(Client):
    def __init__(self, client_id, firstname, lastname, subscription_info, client_status):
        super().__init__(client_id, firstname, lastname, subscription_info, client_status)
        self.category = "All Star client"
        self.benefits = ["25 requests per hour", "5 power search per month", "12 tailor-made advice per year"]

    def category_upgrade(self):
        from flask import request
        new_category = request.args.get("search")
        if new_category == "Rookie" or new_category == "rookie":
            client = Rookie(self.client_id, self.firstname, self.lastname, self.subscription, self.client_status)
        elif new_category == "Hall of fame" or new_category == "hall of fame":
            client = AllStar(self.client_id, self.firstname, self.lastname, self.subscription, self.client_status)


class HallOfFame(Client):
    def __init__(self, client_id, firstname, lastname, subscription_info, client_status):
        super().__init__(client_id, firstname, lastname, subscription_info, client_status)
        self.category = "Hall of Fame client"
        self.benefits = ["unlimited requests per hour", "unlimited power search per month",
                         "unlimited tailor-made advice per year"]

    def category_upgrade(self):
        from flask import request
        new_category = request.args.get("search")
        if new_category == "All star" or new_category == "all star" or new_category == "All Star":
            client = AllStar(self.client_id, self.firstname, self.lastname, self.subscription, self.client_status)
        elif new_category == "Rookie" or new_category == "rookie":
            client = AllStar(self.client_id, self.firstname, self.lastname, self.subscription, self.client_status)


class Subscription:
    def __init__(self, type, start_date, expiry_date, active):
        self.type = type
        self.start_date = start_date
        self.expiry_date = expiry_date
        self.active = active