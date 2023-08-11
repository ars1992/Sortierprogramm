import json
class Conf:
    def __init__(self):
        self.__pfad = ".conf/conf.json"

    def __json_daten_laden_lesen(self):
        with open(self.__pfad, "r") as file:
            daten = json.load(file)
        return daten

    def __json_daten_laden_schreiben(self):
        ...

    def __aktuelle_conf_anzeigen(self):
        daten = self.__json_daten_laden_lesen()
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
            self.__conf_erstellen_quellordner()
        if auswahl == "2":
            ...
            #TODO
        if auswahl == "3":
            self.__aktuelle_conf_anzeigen()


    def __conf_erstellen_quellordner(self):
        pfad_zielordner = input("Pfad des Quellordners: ")
        aktuelle_daten = self.__json_daten_laden_lesen()
        aktuelle_daten[0]["quellordner"].append(pfad_zielordner)
        print(aktuelle_daten)
        with open(self.__pfad, "w") as file:
            print(json.dumps(aktuelle_daten, indent=1, ensure_ascii=False), file=file)



    @staticmethod
    def json_zurück_setzen(self):
        daten = [{"quellordner": [], "zielordner": []}]
        with open(self.__pfad, "w") as file:
            print(json.dumps(daten, indent=2, ensure_ascii=False), file=file)
