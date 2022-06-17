import json
from src.models.clients import Rookie, AllStar, HallOfFame


def load_clients():
    clients = []

    with open(r'C:\Users\alejo\trabajo practico fund info 2022\src\db\clients.json', 'r') as file:
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
                        client['client_status'],
                        client['category'],
                        client['subscription_info']
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
                        client['client_status'],
                        client['category'],
                        client['subscription_info']
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
                        client['client_status'],
                        client['category'],
                        client['subscription_info']
                    )
                )
    return clients



