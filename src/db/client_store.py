import json


def store_client_file(client):
    with open(r'C:\Users\alejo\trabajo practico fund info 2022\src\db\test.json', 'w') as store_file:
        json.dump(client, store_file)
        print('client stored')
