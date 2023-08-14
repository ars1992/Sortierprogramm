import json
import os
import term


class Conf:
    def __init__(self):
        self.__pfad = ".conf/conf.json"

    def __json_daten_laden_lesen(self):
        with open(self.__pfad, "r") as file:
            daten = json.load(file)
        return daten

    def __aktuelle_conf_anzeigen(self):
        daten = self.__json_daten_laden_lesen()
        print("Der aktuelle Quellordner ist:")
        for i in daten[0]["quellordner"]:
            print(i)
        print("Der aktuelle Zielordner ist:")
        for i, v in daten[0]["zielordner"].items():
            print(i, v)
        print("Die aktuellen Unterordner sind:")
        for i in daten[0]["unterordner"]:
            print(i)

    def __conf_erstellen_pfade_quellordner(self):
        while True:
            pfad_ordner = input("Pfad des Quellordner: ")
            if pfad_ordner == "":
                return
            aktuelle_daten = self.__json_daten_laden_lesen()
            aktuelle_daten[0]["quellordner"].append(pfad_ordner)
            with open(self.__pfad, "w") as file:
                print(json.dumps(aktuelle_daten, indent=1, ensure_ascii=False), file=file)

    def __conf_erstellen_pfade_zielordner(self):
        while True:
            pfad_ordner = input(f"Pfad des Zielordner: ")
            if pfad_ordner == "":
                return
            ordnername = pfad_ordner.split("\\")[-1]
            aktuelle_daten = self.__json_daten_laden_lesen()
            aktuelle_daten[0]["zielordner"][ordnername] = pfad_ordner
            with open(self.__pfad, "w") as file:
                print(json.dumps(aktuelle_daten, indent=1, ensure_ascii=False), file=file)

    def __conf_unterordner_erstellen(self):
        while True:
            name_unterordner = input("Wie soll der unterordner heißen: ").upper()
            conf_zielordner = self.conf_daten_aktuelle_pfade("zielordner")
            conf_unterordner = self.conf_daten_aktuelle_pfade("unterordner")
            if name_unterordner == "":
                return
            if name_unterordner not in conf_unterordner:
                aktuelle_daten = self.__json_daten_laden_lesen()
                aktuelle_daten[0]["unterordner"].append(name_unterordner)
                with open(self.__pfad, "w") as file:
                    print(json.dumps(aktuelle_daten, indent=1, ensure_ascii=False), file=file)
                for pfad in conf_zielordner.values():
                    os.mkdir(f"{pfad}\\{name_unterordner}")
            else:
                print("Ordner bereits vorhanden.")

    def __conf_bestehendes_verzeichnis_einbinden(self):
        verzeichnis = input("Pfad zum Stammordner: ")
        ordner = os.listdir(verzeichnis)
        aktuelle_daten = self.__json_daten_laden_lesen()
        for i in ordner:
            aktuelle_daten[0]["zielordner"][i] = f"{verzeichnis}\\{i}"
        for i in self.__unterordner_auflisten(verzeichnis):
            aktuelle_daten[0]["unterordner"].append(i)
        with open(self.__pfad, "w") as file:
            print(json.dumps(aktuelle_daten, indent=1, ensure_ascii=False), file=file)
        for i in aktuelle_daten[0]["unterordner"]:
            for j in aktuelle_daten[0]["zielordner"].values():
                try:
                    os.mkdir(f"{j}\\{i}")
                except FileExistsError:
                    continue

    def __unterordner_auflisten(self, pfad=""):
        unterordner = set()
        for i in os.listdir(pfad):
            for j in os.listdir(f"{pfad}\\{i}"):
                if "." not in j:
                    unterordner.add(j)
        return unterordner

    def auswahl_einstellungen(self):
        while True:
            print("---- Menue 2 ----")
            print("Was möchtest du tun?")
            print("Mit Enter beenden!")
            print("1 - Neuer Quellordner anlegen")
            print("2 - Neuer Zielordner anlegen")
            print("3 - Neuer Unterordner anlegen und erstellen")
            print("4 - Bestehendes Verzeichnis als Ziel einbinden")
            print("5 - Aktuelle conf anzeigen")
            print("6 - Zurück")
            auswahl = input("Deine Wahl: ")
            if auswahl == "1":
                self.__conf_erstellen_pfade_quellordner()
            if auswahl == "2":
                self.__conf_erstellen_pfade_zielordner()
            if auswahl == "3":
                self.__conf_unterordner_erstellen()
            if auswahl == "4":
                self.__conf_bestehendes_verzeichnis_einbinden()
            if auswahl == "5":
                self.__aktuelle_conf_anzeigen()
            if auswahl == "6":
                term.terminal()
            if auswahl == "":
                return

    def conf_daten_aktuelle_pfade(self, ordner):
        daten = self.__json_daten_laden_lesen()
        return daten[0][ordner]

    def conf_vorhanden(self):
        if len(self.conf_daten_aktuelle_pfade("quellordner")) <= 0 and \
                len(self.conf_daten_aktuelle_pfade("zielordner")) <= 0:
            self.__aktuelle_conf_anzeigen()
            return False
        return True

    def get_pfad(self):
        return self.__pfad

    # Testmethoden
    @staticmethod
    def json_zurück_setzen():
        daten = [{"quellordner": [], "zielordner": {}, "unterordner": []}]
        with open(".conf/conf.json", "w") as file:
            print(json.dumps(daten, indent=2, ensure_ascii=False), file=file)
