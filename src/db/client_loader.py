import json
from src.models.clients import Subscription, Rookie, AllStar, HallOfFame


def load_clients():
    clients = []

    with open('src/db/clients.json', 'r') as file:
        clients_json = json.load(file)
        for client in clients_json:
            if client['category'] == 'Rookie':
                clients.append(
                    Rookie(
                        client['client_id'],
                        client['first_name'],
                        client['last_name'],
                        client['date_of_birth'],
                        client['email'],
                        Subscription(
                            client['subscription_info']['type'],
                            client['subscription_info']['start_date'],
                            client['subscription_info']['expiry_date'],
                            client['subscription_info']['active'],
                        ),
                        client['client_status'],
                        client['category']
                    )
                )
            elif client['category'] == 'All Star':
                clients.append(
                    AllStar(
                        client['client_id'],
                        client['first_name'],
                        client['last_name'],
                        client['date_of_birth'],
                        client['email'],
                        Subscription(
                            client['subscription_info']['type'],
                            client['subscription_info']['start_date'],
                            client['subscription_info']['expiry_date'],
                            client['subscription_info']['active'],
                        ),
                        client['client_status'],
                        client['category']
                    )
                )
            elif client['category'] == 'Hall of Fame':
                clients.append(
                    HallOfFame(
                        client['client_id'],
                        client['first_name'],
                        client['last_name'],
                        client['date_of_birth'],
                        client['email'],
                        Subscription(
                            client['subscription_info']['type'],
                            client['subscription_info']['start_date'],
                            client['subscription_info']['expiry_date'],
                            client['subscription_info']['active'],
                        ),
                        client['client_status'],
                        client['category']
                    )
                )
    return clients


print(load_clients())
