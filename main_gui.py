from tkinter import *
from functools import partial
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import sys
import time
import hashlib
import requests
import json
import webbrowser



def gui_scanning_file(file_user):
    m = hashlib.md5()
    result = m.hexdigest()
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': 'b7a646d7d89e708cb7fb483d070d10976cabb2a61a26cb7387ea87079b5afeda'}
    files = { 'file' : ( result, open( file_user , 'rb'))}


    response = requests.post(url, files=files, params=params)
    link = response.json()["permalink"] 
    print("Votre naviguateur va s'ouvrir a l'adresse suivante : ", link + "si il ne s'ouvre pas, veuillez directement copier coller le lien dans votre naviguateur")
    time.sleep(2)
    webbrowser.open(link)
    

def selectfileonpc():
    file = askopenfilename()
    gui_scanning_file(file)

def sa_fonctionnait_pas_autrement():
    file_user = saisir.get()
    gui_scanning_file(file_user)


#CREATION FENETRE
gui = Tk()
gui.title("GodZilla")
gui.minsize(720, 400)
gui.maxsize(720, 400)
gui.geometry("720x400")
gui.config(background='#3A3837')

#title
label_title = Label(gui, text="Welcome on GodZilla", font=('Courrier', 40), bg="#3A3837", fg="white")
label_title.pack()

#autor
label_autor = Label(gui, text="Dev By Baki", font=('Courrier', 15), bg="#3A3837", fg="white")
label_autor.place(x=280, y=80)

#consigne
label_consign = Label(gui, text="Choisissez votre fichier ou écrivez son chemin d'accès ", font=('Courier', 12), bg="#3A3837", fg="white")
label_consign.place(x=90, y=125)


#choice button
saisir= StringVar()
entry_file = Entry(gui, textvariable=saisir)
entry_file.place(x=270, y=190)
file_user = saisir.get()
print(file_user)


search = Button(gui, text="Select", font=('Courrier', 10), bg="#3A3837", fg="white", command=selectfileonpc).place(x=410, y=184)

buton_scan = Button(gui, text="Scanner", font=('Courrier', 10), bg="#3A3837", fg="white", command=sa_fonctionnait_pas_autrement)
buton_scan.place(x=300, y=270)

gui.mainloop()

