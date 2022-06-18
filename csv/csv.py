import csv
clients = [
    ('Alejo', 'Di Lelle', 23, 'adilelle@ucema.edu.ar'),
    ('Kevin', 'Harnan', 22, 'kharnan@ucema.edu.ar'),
    ('Ignacio', 'Freiria', 21, 'ifreiria@ucema.edu.ar'),
    ('Catalina', 'Dapena', 20, 'cdapena@ucema.edu.ar')
]

with open(r'C:\csv\prueba.csv', 'w', newline='\n') as archivo:
    writer = csv.writer(archivo, delimiter=';')
    for client in clients:
        writer.writerow(client)
