# ESCRITURA EN DICCIONARIOS

import csv

clients = [
    ('Alejo', 'Di Lelle', 23, 'adilelle@ucema.edu.ar'),
    ('Kevin', 'Harnan', 22, 'kharnan@ucema.edu.ar'),
    ('Ignacio', 'Freiria', 21, 'ifreiria@ucema.edu.ar'),
    ('Catalina', 'Dapena', 20, 'cdapena@ucema.edu.ar')
]

with open('prueba.csv','w', newline='\n') as archivo:
    campos = ['first_name', 'last_name', 'date_of_birth', 'email']
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    for first_name, last_name, date_of_birth, email in clients:
        writer.writerow({
            'first_name':first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'email': email
        })

archivo.close()
del (archivo)

# LECTURA EN DICCIONARIOS

with open('prueba.csv','r', newline='\n') as archivo:
    reader = csv.DictReader(archivo)
    for client in reader:
        print(client['first_name'],
              client['last_name'],
              client['date_of_birth'],
              client['email'])