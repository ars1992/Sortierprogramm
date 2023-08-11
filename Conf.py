import json
class Conf:
    def __init__(self):
        self.__pfad = ".conf/conf.json"

    def __json_daten_laden(self):
        with open(self.__pfad, "r") as file:
            daten = json.load(file)
        return daten
    def __aktuelle_conf_anzeigen(self):
        daten = self.__json_daten_laden()
        print(daten)
        print("Der aktuelle Quellordner ist:")
        for i in daten[0]["quellordner"]:
            print(i)
        print("Der aktuelle Zielordner ist:")
        for i in daten[0]["zielordner"]:
            print(i)


    def auswahl_einstellungen(self):
        print("Was möchtest du tun?")
        print("1 - Neuer Quellordner anlegen")
        print("2 - Neuer Zielordner anlegen")
        print("3 - Aktuelle conf anzeigen")
        auswahl = input("Deine Wahl: ")
        if auswahl == "1":
            #TODO
            ...
        if auswahl == "2":
            ...
            #TODO
        if auswahl == "3":
            self.__aktuelle_conf_anzeigen()


    def __conf_erstellen_quellordner(self):
        pfad_zielordner = input("Pfad des Quellordners: ")


