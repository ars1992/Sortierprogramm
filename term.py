from Conf import Conf
from Sortierer import Sortierer


def hilfe():
    print("Hi schön das du da bist")
    print("Was möchtest du tun?")
    print("Mit Enter beenden!")
    print("1 - Dateien einsortieren")
    print("2 - Einstellungen")

def terminal():
    conf = Conf()
    if not conf.conf_vorhanden():
        conf.auswahl_einstellungen()
    hilfe()
    while True:
        print("---- Menue 1 ----")
        print("h - Hilfe")
        auswahl = input("Deine Wahl: ")
        if auswahl == "1":
            sort = Sortierer()
            sort.zielordner_durchlaufen_und_einsortieren()
            print("Dateien wurden Einsortiert")
        if auswahl == "2":
            conf.auswahl_einstellungen()
        if auswahl.upper() == "H":
            hilfe()
        if auswahl == "":
            return
        print()

