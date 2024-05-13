import time
import csv
import os
from random import choices
import sqlite3
from tkinter import Button, Entry, IntVar, Label, StringVar, Tk, filedialog, messagebox, ttk
from tkinter.constants import CENTER, HORIZONTAL
from tkinter.ttk import Style
import pandas as pd
import generator
import unicodedata

# Crear Base de datos para almarcernar las urls
# pyinstaller --onefile --windowed --icon=icon.ico url-generator.py


def connect():
    currendirectory = os.getcwd()
    if not os.path.exists(currendirectory + '\\db'):
        os.makedirs(currendirectory+'\\db')
    conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, process TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS temp (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, process TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS urlmaps (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, process TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS coordinates (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, startlat TEXT, startlon TEXT, endlat TXT, endlon TEXT , distance TEXT, cid TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS project (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS medium (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), medium VARCHAR(255))'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS campaign (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), campaign VARCHAR(255))'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS terms (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,  keyword TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS source (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,  source TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS google (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,  version TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS language (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,  language TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS random (id INTEGER PRIMARY KEY AUTOINCREMENT, random VARCHAR(255))'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS domains (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) ,domain VARCHAR(255))'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS sa (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) , sa TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS rct (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) , rct TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS esrc (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) , esrc TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS cad (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) , cad TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS uact (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) , uact TEXT)'
    )
    cur.execute(
        'CREATE TABLE IF NOT EXISTS ved (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) , ved TEXT)'
    )
    cur.execute(
        'INSERT INTO random (random) VALUES ("&gl=ES"), ("&hl=ES"), ("&lr=lang_ar"), ("&cr=mx")'
    )
    conn.commit()
    conn.close()


def close_window():
    root.destroy()


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

# funcion para cargar el excel


def upload_action(projectname, event=None):
    if projectname == "":
        messagebox.showwarning(message="Empty Project Name", title="Warning")
        return False
    currendirectory = os.getcwd()
    conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM terms WHERE name=?;", (projectname,))
    row = cur.fetchone()
    if row != None:
        messagebox.showwarning(message="This project name is already in use")
        return False
    conn.close()
    currendirectory = os.getcwd()
    conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO project VALUES (NULL,?)",
                (projectname,))
    conn.commit()
    conn.close()
    filename = filedialog.askopenfilename()
    data = pd.read_excel(filename, sheet_name=None, dtype=str)
    # save data from excel whit pandas to save in data base
    # Get tab 1 Keywords
    keywords = data['Keywords'].values.tolist()
    totalkeywords = len(keywords)
    p = 14 / totalkeywords
    for k in keywords:
        currendirectory = os.getcwd()
        conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO terms VALUES (NULL,?,?)",
                    (projectname, k[0].replace(" ", "%20")))
        conn.commit()
        conn.close()
        print(k[0].replace(" ", "%20"))
        progress_bar['value'] += p
        root.update_idletasks()
    # get tab 2 Google location Servers
    googlevs = data['Google-v'].values.tolist()
    totalgoogle = len(googlevs)
    o = 14 / totalgoogle
    for gv in googlevs:
        currendirectory = os.getcwd()
        conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO google VALUES (NULL,?,?)",
                    (projectname, gv[0]))
        conn.commit()
        conn.close()
        print(gv)
        progress_bar['value'] += o
        root.update_idletasks()
    # Google Maps
    coordinates = data['Google-maps'].values.tolist()
    print(coordinates)
    for c in coordinates:
        currendirectory = os.getcwd()
        conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO coordinates VALUES (NULL,?,?,?,?,?,?,?)",
                    (projectname, c[0], c[1], c[2], c[3], c[4], c[5]))
        conn.commit()
        conn.close()
        # get tab 7 Languages
    languages = data['Language'].values.tolist()
    totallanguages = len(languages)
    a = 14 / totallanguages
    for l in languages:
        language = "&"+l[1]+"="+l[2]
        currendirectory = os.getcwd()
        conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO language VALUES (NULL,?,?)",
                    (projectname, language))
        conn.commit()
        conn.close()
        print(l)
        progress_bar['value'] += a
        root.update_idletasks()
    progress_bar['value'] = 100
    messagebox.showinfo(message='Load Complete', title="Complete")


def generator_url():
    quantity1 = quantity.get()
    select_project = choice_var.get()
    if select_project == "Select One Project":
        messagebox.showwarning(
            message="Please Select a Project", title="0 Links generates")
    if quantity1 == 0:
        messagebox.showwarning(
            message="Please indicate the number of links", title="0 Links generates")
    else:
        generator.generate_urls(quantity1, select_project)


def generator_maps():
    select_project = choice_var.get()
    if select_project == "Select One Project":
        messagebox.showwarning(
            message="Please Select a Project", title="0 Links generates")
    else:
        generator.mapgenerator_urls(select_project)


def export_csv():
    select_project = choice_var.get()
    if select_project == "Select One Project":
        messagebox.showwarning(
            message="Please Select a Project", title="0 Links generates")
    else:
        currendirectory = os.getcwd()
        conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM urls WHERE name=?",
                    (select_project,))
        urls = cur.fetchall()
        conn.commit()
        conn.close()
        microtime = round(time.time() * 1000)
        if not os.path.exists(currendirectory + '\\export'):
            os.makedirs(currendirectory+'\\export')
        with open(currendirectory+'\\export\\' + select_project + '-' + str(microtime) + '-urls.txt', 'a', encoding='utf8', newline='') as file:
            for l in urls:
                file.write(l[2]+"\n")
            messagebox.showinfo(message="Export Complete", title="Succeed")


def export_maps():
    select_project = choice_var.get()
    if select_project == "Select One Project":
        messagebox.showwarning(
            message="Please Select a Project", title="0 Links generates")
    else:
        currendirectory = os.getcwd()
        conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM urlmaps WHERE name=?",
                    (select_project,))
        urls = cur.fetchall()
        conn.commit()
        conn.close()
        microtime = round(time.time() * 1000)
        if not os.path.exists(currendirectory + '\\export'):
            os.makedirs(currendirectory+'\\export')
        with open(currendirectory+'\\export\\' + select_project + '-' + str(microtime) + '-maps-urls.txt', 'a', encoding='utf8', newline='') as file:
            for l in urls:
                file.write(l[2]+"\n")
            messagebox.showinfo(message="Export Complete", title="Succeed")


root = Tk()
connect()
root.title("ThUG")
root.config(bg='#9FB9C6')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
s = Style()
s.configure('My.TFrame', background='#FEEFDD')
center_window(300, 300)
tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent, style='My.TFrame')
tab2 = ttk.Frame(tab_parent, style='My.TFrame')
tab3 = ttk.Frame(tab_parent, style='My.TFrame')
tab_parent.add(tab1, text="Load Data")
tab_parent.add(tab2, text="Link Generator")
tab_parent.add(tab3, text="Maps Link Generator")
tab_parent.pack(expand=1, fill='both')
# add first tab
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_rowconfigure(0, weight=1)
label_name = Label(tab1, text="Project Name", bg='#FEEFDD', fg='#FF4000',
                   font=('helvetica', 12, 'bold'))
label_name.grid(row=1, column=1, pady=6)
projectname = StringVar()
input_name = Entry(tab1, textvariable=projectname,
                   justify=CENTER, font=('helvetica', 12, 'bold'))
input_name.grid(row=2, column=1, padx=10, pady=20, ipadx=30,
                ipady=6)
upload_buttom = Button(tab1, text="Upload Excel File", command=lambda: upload_action(projectname.get()), bg="#50B2C0",
                       fg="white", width=41, height=4)
upload_buttom.grid(row=4, column=1,)
progress_label = Label(tab1, text="Progress Bar", bg='#FEEFDD', fg='#FF4000',
                       font=('helvetica', 12, 'bold'))
progress_label.grid(row=5, column=1)
progress_bar = ttk.Progressbar(
    tab1, orient=HORIZONTAL, length=300, mode='determinate')
progress_bar.grid(row=6, column=1)

# add second tab
currendirectory = os.getcwd()
conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
cur = conn.cursor()
cur.execute("SELECT * FROM project")
rows = cur.fetchall()
conn.commit()
conn.close()
choices_values = []
choice_var = StringVar(tab2)
choice_var.set("Select One Project")
for row in rows:
    choices_values.append(row[1])

label_selec = Label(tab2, text="Select Project", bg='#FEEFDD',
                    fg="#FF4000", font=('helvetica', 12, 'bold'))
label_selec.grid(column=1, row=1, pady=10)
choices = ttk.Combobox(tab2, values=choices_values, textvariable=choice_var)
choices.grid(column=1, row=2, padx=10, pady=10)
label_number = Label(tab2, text="Insert the amount of links", bg='#FEEFDD',
                     fg="#FF4000", font=('helvetica', 12, 'bold'))
label_number.grid(column=1, row=3, padx=10, pady=10)
quantity = IntVar()
number_input = Entry(tab2, textvariable=quantity,
                     justify=CENTER, font=('helvetica', 12, 'bold'))
number_input.grid(column=1, row=4)
generate_buttom = Button(tab2, text="Generate URLS",
                         command=generator_url, bg="#50B2C0", fg='white', width=41, height=4)
generate_buttom.grid(column=1, row=5)
export_buttom = Button(tab2, text="Export to  .TXT",
                       command=export_csv, bg="green", fg='white', width=41, height=2)
export_buttom.grid(column=1, row=6)

# add Third tab
currendirectory = os.getcwd()
conn = sqlite3.connect(currendirectory+"\\db\\newdatabase.db")
cur = conn.cursor()
cur.execute("SELECT * FROM project")
rows = cur.fetchall()
conn.commit()
conn.close()
choices_values = []
choice_var = StringVar(tab3)
choice_var.set("Select One Project")
for row in rows:
    choices_values.append(row[1])

label_selec = Label(tab3, text="Select Project", bg='#FEEFDD',
                    fg="#FF4000", font=('helvetica', 12, 'bold'))
label_selec.grid(column=1, row=1, pady=10)
choices = ttk.Combobox(tab3, values=choices_values, textvariable=choice_var)
choices.grid(column=1, row=2, padx=10, pady=10)
label_selec = Label(tab3, text="Select Project", bg='#FEEFDD',
                    fg="#FF4000", font=('helvetica', 12, 'bold'))
label_selec.grid(column=1, row=1, pady=10)
choices = ttk.Combobox(tab3, values=choices_values, textvariable=choice_var)
choices.grid(column=1, row=2, padx=10, pady=10)
generate_buttom = Button(tab3, text="Generate URLS And Export",
                         command=generator_maps, bg="#50B2C0", fg='white', width=41, height=4)
generate_buttom.grid(column=1, row=5)
export_buttom = Button(tab3, text="Export to  .TXT",
                       command=export_maps, bg="green", fg='white', width=41, height=2)
export_buttom.grid(column=1, row=6)

root.mainloop()
