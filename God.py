#coding:utf-8
import time
import os
try:
    import tkinter
except:
    a = 1
    print("GodZilla n'a pas reconnu le mondule Tkinter sur votre machine")
    print("Sans se module, GodZilla ne peut pas lancer son Interface Graphique.")
    print("Voulez vous l'installer ? \n")
    print("1 : Oui")
    print("2 : Non")
    print("Si vous êtes sur un system Windows, GodZilla ne permet pas d'installer Tkinter.")
    print("Vous devrez donc l'installer vous même.\n")
    k = input(" -- > ")
    if k == "1":
        os.system("sudo apt install python-tk")
        os.system("sudo apt install python-imaging-tk")
        os.system("sudo apt install python3-tk")

    elif k == "2":
        print("Vous pouvez continuer à utiliser GodZilla ")
        print("Mais son interface graphique sera désactivé")
        time.sleep(5)
        
    
    else:
        print("Choix introuvable.")


import sys
import hashlib
import requests
import json
import webbrowser


def present():

    print("""

      ________           ._____________.__.__  .__          
     /  _____/  ____   __| _/\____    /|__|  | |  | _____   
    /   \  ___ /  _ \ / __ |   /     / |  |  | |  | \__  \  
    \    \_\  (  <_> ) /_/ |  /     /_ |  |  |_|  |__/ __ \_
     \______  /\____/\____ | /_______ \|__|____/____(____  /
            \/            \/         \/                  \/ 
    
                       [Dev By Baki]
                          [V 1.0]


    """)


present()
time.sleep(2)



def option():
    print("""
          [ Basic Command ]

             [  help             = Show help                          ]
             [  info             = Informatique about GodZilla        ]

          [ GodZilla Command ]

            [  scan             = Scan the file with Virus Total API ]
            [  gui              = Start the GUI ( simpler )          ] 
            [  hash             = Show the hash of the file          ]

          [ Optional Command ]

            [  clear            = clean the interface                ]
            [  banner           = print the banner of GodZilla       ]
    
    
    """)

option ()
time.sleep(1)





#DEFINIR LE HASH D'UN FICHIER
def show_hash(file_user):
    m = hashlib.md5()
    reslut = m.hexdigest()
    print("The Hash is -- > ",reslut)  




#API VIRUS TOTAL 
def scan_total(file_user):
    m = hashlib.md5()
    result = m.hexdigest()
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': 'b7a646d7d89e708cb7fb483d070d10976cabb2a61a26cb7387ea87079b5afeda'}
    files = { 'file' : ( result, open( file_user , 'rb'))}


    response = requests.post(url, files=files, params=params)
    link = response.json()["permalink"] 
    print("Votre naviguateur va s'ouvrir a l'adresse suivante : ", link + "si il ne s'ouvre pas, veuillez directement copier coller le lien dans votre naviguateur")
    time.sleep(4)
    webbrowser.open(link)






#INFORMATION :
def information_godzilla_fr():
    print("""
        [!] GodZilla Information Tools [!]

        
        GodZilla est un outil de protection contre les malwares ( virus , programme malveillant ).
        Il utilise l'API de virus total ( https://www.virustotal.com/ ) afin de scanner les hash
        des fichiers demander. Virus totale fait analyser ce hash par envrions 60 anti virus.
        Nous conseillons de vous rappeler la provenance d'un fichier lorsqu'il est détécté par
        1 anti virus. GodZilla lance une alerte également lorsque vous téléchargez un fichier
        en vous conseillant de faire scanner ce dernier avec l'outil.
        GodZilla possède également une interface graphique, plus simple pour les personnes
        n'ayant pas pour habitude d'utiliser la ligne de commande.  
    
    """)


def information_godzilla_agl():
    print("""
    
    [!] GodZilla Information Tools [!]


    GodZilla is a malware protection tool (virus, malware).
    It uses the Total Virus API (https://www.virustotal.com/) to scan for hashes
    files ask. Total virus has this hash analyzed by around 60 anti viruses.
    We advise you to remember the source of a file when it is detected by
    1 anti virus. GodZilla also alerts when you download a file
    advising you to scan the latter with the tool.
    GodZilla also has a simpler graphical interface for people
    not used to using the command line.

    """)





def main():
    q = True
    while q:
        user = input("GodZilla -- > ")

        #BASIQUE COMMANDE

        if user == "help":
            option()
        elif user == "clear":

            if exploit == '1':
                os.system("clear")
            elif exploit == '2':
                os.system('cls')
            else:
                print("GodZilla ne reconnait pas votre OS, veuillez relancer le programme")

        elif user == "info":
            print("Please Choose a language : ")
            print('French  : 1')
            print("English : 2")
            choice = input('Your Choice -- > ')
            if choice == "1":
                information_godzilla_fr()
            elif choice == "2":
                information_godzilla_agl()
            else:
                print("Error, try again")
        
        elif user == "banner":
            present()


        #OPTION GODZILLA
        elif user == "hash":
            file_user = str(input('Name Of The File -- > '))
            show_hash(file_user)
        
        elif user == "scan":
            file_user = str(input("Name Of The File -- > "))
            scan_total(file_user)
        
        elif user == "gui":
            print("Starting GodZilla Gui . . .")
            time.sleep(1)
            os.system("python3 main_gui.py")
               




        else:
            print("GodZilla -- > Commande Introuvable")








#CHOIX DE L'OS

print("Quel est votre système d'exploitation : \n")
print(' 1 = Linux ')
print(" 2 = windows\n")
exploit = str(input(" -- > "))
if exploit == '1':
    print()
    print("Vous êtes maintenant prêt à utiliser GodZilla !\n ")
    time.sleep(2)
    main()
elif exploit == '2':
    print()
    print("Vous êtes maintenant prêt à utiliser GodZilla ! \n")
    time.sleep(2)
    main()
else:
    print("Votre choix est indisponible, veuillez relancer GodZilla.")