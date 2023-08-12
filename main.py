from Conf import *
from Sortierer import Sortierer

#Conf.json_zurück_setzen()

def hilfe():
    print("Hi schön das du da bist")
    print("Was möchtest du tun?")
    print("Mit Enter beenden!")
    print("1 - Dateien einsortieren")
    print("2 - Einstellungen")
def terminal():
    hilfe()
    while True:
        print("h - Hilfe")
        auswahl = input("Deine Wahl: ")
        if auswahl == "1":
            sort = Sortierer()
            sort.zielordner_durchlaufen_und_einsortieren()
            print("Dateien wurden Einsortiert")
        if auswahl == "2":
            conf = Conf()
            conf.auswahl_einstellungen()
        if auswahl.upper() == "H":
            hilfe()
        if auswahl == "":
            return
        print()


terminal()







