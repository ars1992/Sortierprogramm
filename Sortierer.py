import shutil, os

from Conf import Conf


class Sortierer:
    def __init__(self):
        self.conf = Conf()
        self.pfad = self.conf.get_pfad()
        self.quellordner = self.conf.conf_daten_aktuelle_pfade("quellordner")
        self.zielordner = self.conf.conf_daten_aktuelle_pfade("zielordner")

    def fachwahl(fach="", pfad=""):
        try:
            if datei_split[1].upper() == fach: # Fach abfragen
                if datei_split[2].upper() == "ON":
                    shutil.move(source + "\\" + datei, pfad + "\\" + "OneNote" + "\\" + datei)
                elif datei_split[2].upper() == "MO":
                    shutil.move(source + "\\" + datei, pfad + "\\" + "Moodle" + "\\" + datei)
                elif datei_split[2].upper() == "IN":
                    shutil.move(source + "\\" + datei, pfad + "\\" + "Inetinfo" + "\\" + datei)
                elif datei_split[2].upper() == "PA":
                    shutil.move(source + "\\" + datei, pfad + "\\" + "Papier" + "\\" + datei)
                elif datei_split[2].upper() in ("ZU", "MI", "KL"):
                    shutil.move(source + "\\" + datei, pfad + "\\" + "Klausur" + "\\" + datei)
                elif datei_split[2].upper() == "BI":
                    shutil.move(source + "\\" + datei, pfad + "\\" + "Bilder" + "\\" + datei)
                elif datei_split[2].upper() == "PR":
                    shutil.move(source + "\\" + datei, pfad + "\\" + "Präsentation" + "\\" + datei)
                else:
                    shutil.move(source + "\\" + datei, pfad + "\\" + datei)

        except FileNotFoundError:
            print("Error")
            print(datei)
            input("Weiter mit Enter")

    files = os.listdir(source)
    for datei in files:
        try:
            datei_split = datei.split("_")
            for f, p in dic_feacher.items():
                fachwahl(fach=f, pfad=p)
        except IndexError:
            print("Fehlerhafter Dateiname")
            print(datei)
            x = input("Weiter mit Enter")