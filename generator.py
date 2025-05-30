import os
from os import utime
import sqlite3
from tkinter import messagebox
import random


def generate_urls(quantity, project_name):
    # conectar con la base de datos
    currendirectory = os.getcwd()
    conn = sqlite3.connect(currendirectory+"\\db\\urldatabase.db")
    cur = conn.cursor()
    url_initials = ['https://www.', 'https://', 'http://www.', 'http://']
    utum_list = ['utm_source=', 'utm_medium=',
                'utm_campaign=', 'utm_term=', 'utm_content=']
    i = 0
    while i < quantity:
        random.shuffle(url_initials)
        # Google
        sql = 'SELECT * FROM google WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(sql, (project_name,))
        googlelocal = cur.fetchone()
        # Domains
        query_domains = 'SELECT * FROM domains WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(query_domains, (project_name,))
        domain = cur.fetchone()
        # languages
        query_languages = 'SELECT * FROM language WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(query_languages, (project_name,))
        language = cur.fetchone()
        # buscar los utum elementos en la base de datos
        # Source
        query_source = 'SELECT * FROM source WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(query_source, (project_name,))
        source = cur.fetchone()
        # Medium
        query_medium = 'SELECT * FROM medium WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(query_medium, (project_name,))
        medium = cur.fetchone()
        # Campaing
        query_campaing = 'SELECT * FROM campaign WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(query_campaing, (project_name,))
        campaing = cur.fetchone()
        # Term
        query_term = 'SELECT * FROM terms WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(query_term, (project_name,))
        term = cur.fetchone()
        utum_list_process = []
        utum_list_process.append(utum_list[0]+source[2])
        utum_list_process.append(utum_list[1]+medium[2])
        utum_list_process.append(utum_list[2]+campaing[2])
        utum_list_process.append(utum_list[3]+term[2])
        utum_list_process.append(utum_list[4]+medium[2])
        random.shuffle(utum_list_process)
        # search random variants from data base
        # sa
        sa = 'SELECT * FROM sa WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(sa, (project_name,))
        v_sa = cur.fetchone()
        # rct
        rct = 'SELECT * FROM rct WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(rct, (project_name,))
        v_rct = cur.fetchone()
        # esrc
        esrc = 'SELECT * FROM esrc WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(esrc, (project_name,))
        v_esrc = cur.fetchone()
        # cad
        cad = 'SELECT * FROM cad WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(cad, (project_name,))
        v_cad = cur.fetchone()
        # uact
        uact = 'SELECT * FROM uact WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(uact, (project_name,))
        v_uact = cur.fetchone()
        # ved
        ved = 'SELECT * FROM ved WHERE name=? ORDER BY RANDOM() LIMIT 1'
        cur.execute(ved, (project_name,))
        v_ved = cur.fetchone()
        # generate a list whit variant
        variants = []
        variants.append("sa="+v_sa[2])
        variants.append("rct="+v_rct[2])
        variants.append("esrc="+v_esrc[2])
        variants.append("cad="+v_cad[2])
        variants.append("uact="+v_uact[2])
        variants.append("ved="+v_ved[2])
        # randomizer list
        random.shuffle(variants)
        # generate URL
        url_generated = url_initials[0]+googlelocal[2]+'/url?q=' + \
            domain[2]+'/?' + utum_list_process[0]+'&' + \
            utum_list_process[1]+'&'+utum_list_process[2]+'&' + \
            utum_list_process[3]+'&' + \
            utum_list_process[4]+'&'+language[2] + \
            '&'+variants[0]+'&'+variants[1]+'&' + \
            variants[2]+'&'+variants[3]+'&'+variants[4]+'&'+variants[5]
        # check if url Exist
        checkurl_query = 'SELECT * FROM urls WHERE url=?'
        cur.execute(checkurl_query, (url_generated,))
        check = cur.fetchone()
        if check == None:
            insert_url = "INSERT INTO urls VALUES (NULL,?,?,?)"
            cur.execute(insert_url, (project_name, url_generated, ""))
            i = i+1

    conn.commit()
    conn.close()
