import shutil, os

from Conf import Conf


class Sortierer:
    def __init__(self):
        self.conf = Conf()
        self.pfad = self.conf.get_pfad()
        self.quellordner = self.conf.conf_daten_aktuelle_pfade("quellordner")
        self.zielordner = self.conf.conf_daten_aktuelle_pfade("zielordner")

    def pfad_erstellen(self, dateiname="", pfad=""):
        return f"{pfad}\\{dateiname}"

    def datei_verschieben(self, dateiname="", ordner=""):
        if dateiname.split("_")[1].upper() == ordner.upper():
            shutil.move(self.pfad_erstellen(dateiname=dateiname, pfad=self.quellordner[0]),
                        self.pfad_erstellen(dateiname=dateiname, pfad=self.zielordner[ordner]))

    # def zielordner_durchlaufen(self):
    #     files = os.listdir(self.quellordner[0])
    #     for datei in files:
    #         for