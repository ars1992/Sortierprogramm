import json
import os


class Conf:
    def __init__(self):
        self.__pfad = ".conf/conf.json"

    def __json_daten_laden_lesen(self):
        with open(self.__pfad, "r") as file:
            daten = json.load(file)
        return daten

    def __aktuelle_conf_anzeigen(self):
        daten = self.__json_daten_laden_lesen()
        print(daten)
        print("Der aktuelle Quellordner ist:")
        for i in daten[0]["quellordner"]:
            print(i)
        print("Der aktuelle Zielordner ist:")
        for i in daten[0]["zielordner"]:
            print(i)

    def __conf_erstellen_pfade_quellordner(self):
        pfad_ordner = input("Pfad des Quellordner: ")
        aktuelle_daten = self.__json_daten_laden_lesen()
        aktuelle_daten[0]["quellordner"].append(pfad_ordner)
        with open(self.__pfad, "w") as file:
            print(json.dumps(aktuelle_daten, indent=1, ensure_ascii=False), file=file)

    def __conf_erstellen_pfade_zielordner(self):
        pfad_ordner = input(f"Pfad des Zielordner: ")
        ordnername = pfad_ordner.split("\\")[-1]
        aktuelle_daten = self.__json_daten_laden_lesen()
        aktuelle_daten[0]["zielordner"][ordnername] = pfad_ordner
        with open(self.__pfad, "w") as file:
            print(json.dumps(aktuelle_daten, indent=1, ensure_ascii=False), file=file)


    def __conf_unterordner_erstellen(self):
        name_unterordner = input("Wie soll der unterordner heißen: ").upper()
        conf_zielordner = self.conf_daten_aktuelle_pfade("zielordner")
        conf_unterordner = self.conf_daten_aktuelle_pfade("unterordner")
        print(conf_unterordner, conf_zielordner)
        if name_unterordner not in conf_unterordner:
            aktuelle_daten = self.__json_daten_laden_lesen()
            aktuelle_daten[0]["unterordner"].append(name_unterordner)
            with open(self.__pfad, "w") as file:
                print(json.dumps(aktuelle_daten, indent=1, ensure_ascii=False), file=file)
            for pfad in conf_zielordner.values():
                os.mkdir(f"{pfad}\\{name_unterordner}")
        else:
            print("Ordner bereits vorhanden.")



    def auswahl_einstellungen(self):
        print("Was möchtest du tun?")
        print("1 - Neuer Quellordner anlegen")
        print("2 - Neuer Zielordner anlegen")
        print("3 - Neuer Unterordner anlegen und erstellen")
        print("4 - Aktuelle conf anzeigen")
        auswahl = input("Deine Wahl: ")
        if auswahl == "1":
            self.__conf_erstellen_pfade_quellordner()
        if auswahl == "2":
            self.__conf_erstellen_pfade_zielordner()
        if auswahl == "3":
            self.__conf_unterordner_erstellen()
        if auswahl == "4":
            self.__aktuelle_conf_anzeigen()

    def conf_daten_aktuelle_pfade(self, ordner):
        daten = self.__json_daten_laden_lesen()
        return daten[0][ordner]

    def get_pfad(self):
        return self.__pfad

    # Testmethoden
    @staticmethod
    def json_zurück_setzen():
        daten = [{"quellordner": [], "zielordner": {}, "unterordner": []}]
        with open(".conf/conf.json", "w") as file:
            print(json.dumps(daten, indent=2, ensure_ascii=False), file=file)
