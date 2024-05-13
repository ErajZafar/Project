import os
from os import utime
import sqlite3
from tkinter import messagebox
import random
from tkinter.constants import FALSE, TRUE
import pandas as pd
import math


def generate_urls(quantity, project_name):
    # conectar con la base de datos
    currendirectory = os.getcwd()
    conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
    cur = conn.cursor()
    url_initials = ['https://www.', 'https://', 'http://www.', 'http://']

    i = 0
    while i < quantity:
        random.shuffle(url_initials)
        # Google
        sql = 'SELECT * FROM google WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(sql, (project_name,))
        googlelocal = cur.fetchone()
        # keywords
        query_term = 'SELECT * FROM terms WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(query_term, (project_name,))
        terms = cur.fetchone()
        terms[2].replace("%20", "+")
        # Url Generator
        # url demo https://www.google.com/search?igu=1&ei=&q=Moon+and+Owl+Marketing
        search_url_generator = url_initials[0] + \
            googlelocal[2]+'/search?igu=1&ei=&q=' + terms[2]
        # check if url Exist
        checkurl_query = 'SELECT * FROM urls WHERE url=?'
        cur.execute(checkurl_query, (search_url_generator,))
        check = cur.fetchone()
        if check == None:
            insert_url = "INSERT INTO urls VALUES (NULL,?,?,?)"
            cur.execute(insert_url, (project_name, search_url_generator, ""))
            i = i+1

    conn.commit()
    conn.close()
    messagebox.showinfo(message="Generate URL Complete", title="Succeed")


def mapgenerator_urls(project_name):
    # conectar con la base de datos
    currendirectory = os.getcwd()
    conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
    cur = conn.cursor()
    url_initials = ['https://www.', 'https://', 'http://www.', 'http://']
    random.shuffle(url_initials)
    # optener todos los datos de la base de datos
    maps_data = 'SELECT * FROM `coordinates` WHERE name=?'
    cur.execute(maps_data, (project_name,))
    rows = cur.fetchall()
    for row in rows:
        cid = row[1]
        startlat = row[2]
        startlon = row[3]
        endlat = row[4]
        endlon = row[5]
        distance = row[6]
        # generar todas las coordenadas
        coordenates = generate_coordenates(
            startlat, startlon, endlat, endlon, distance)
    conn.commit()
    conn.close()
    messagebox.showinfo(message="Generate URL Complete", title="Succeed")


def generate_coordenates(startlat, startlon, endlat, endlon, distance):
    procesar = []
    procesar.append(startlat)
    procesar.append(startlon)
    procesar.append(endlat)
    procesar.append(endlon)
    temporal = []
    millas = 5
    while millas > 2:
        print(procesar)
        for i in range(len(procesar)):
            lat1 = procesar[i]
            lon1 = procesar[i+1]
            lat2 = procesar[i+2]
            lon2 = procesar[i+3]
            result = calculate_coordenates(lat1, lat2, lon1, lon2)
            temporal.append(lat1)
            temporal.append(lon1)
            temporal.append(result['latitude'])
            temporal.append(result['longitude'])
            temporal.append(lat2)
            temporal.append(lon2)
            # se remueve para calcular el siguiente
            procesar.remove(lat1)
            procesar.remove(lon1)
        procesar = []
        for i in range(len(temporal)):
            procesar.append(temporal[i])
        millas = millas-1

    return 'hola'


def calculate_coordenates(lat1, lat2, lon1, lon2):
    # generar coordenadas
    x = 0.0
    y = 0.0
    z = 0.0
    data = {'latitude':  [lat1, lat2],
            'longitude': [lon1, lon2],
            }
    coords_df = pd.DataFrame(
        data, columns=['latitude', 'longitude'])
    for i, coord in coords_df.iterrows():
        latitude = math.radians(float(coord.latitude))
        longitude = math.radians(float(coord.longitude))
        x += math.cos(latitude) * math.cos(longitude)
        y += math.cos(latitude) * math.sin(longitude)
        z += math.sin(latitude)

    total = len(coords_df)
    x = x / total
    y = y / total
    z = z / total
    central_longitude = math.atan2(y, x)
    central_square_root = math.sqrt(x * x + y * y)
    central_latitude = math.atan2(z, central_square_root)
    # format es para dejar los decimales en 5 solamente
    mean_location = {
        'latitude': format(math.degrees(central_latitude), '.5f'),
        'longitude': format(math.degrees(central_longitude), '.5f')
    }
    return mean_location


def calculate_distance(lat1, lon1, lat2, lon2, distance):
    R = 6373.0
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    kilometers = R * c
    # convertir kilometros a millas
    conv_fac = 0.621371
    milles = kilometers * conv_fac
    if float(distance) < milles:
        return FALSE
    else:
        return TRUE
