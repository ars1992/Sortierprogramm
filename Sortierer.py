import shutil, os

from Conf import Conf


class Sortierer:
    def __init__(self):
        self.__conf = Conf()
        self.__pfad = self.__conf.get_pfad()
        self.__quellordner = self.__conf.conf_daten_aktuelle_pfade("quellordner")
        self.__zielordner = self.__conf.conf_daten_aktuelle_pfade("zielordner")

    def __pfad_erstellen(self, dateiname="", pfad=""):
        return f"{pfad}\\{dateiname}"

    def __datei_verschieben(self, dateiname="", ordner="", index=0):
        try:
            if dateiname.split("_")[1].upper() == ordner.upper():
                shutil.move(self.__pfad_erstellen(dateiname=dateiname, pfad=self.__quellordner[index]),
                            self.__pfad_erstellen(dateiname=dateiname, pfad=self.__zielordner[ordner]))
        except IndexError:
            print(f"Felerhafterdateiname von: {dateiname}")
            eingabe = input("Möchtest du die Datei umbenennen (j/n): ")
            if eingabe.upper() == "J":
                self.__datei_umbenennen(dateiname=dateiname)

    def zielordner_durchlaufen_und_einsortieren(self):
        for i in range(0, len(self.__quellordner)):
            files = os.listdir(self.__quellordner[i])
            for dateiname in files:
                for ordner, pfad in self.__zielordner.items():
                    self.__datei_verschieben(dateiname=dateiname, ordner=pfad.split("\\")[-1], index=i)

    def __datei_umbenennen(self, dateiname=None, index=0):
        if dateiname:
            print(f"Aktuellername: {dateiname}")
            neuer_dateiname = input("Neuer Dateiname: ")
            os.rename(f"{self.__quellordner[index]}\\{dateiname}",
                      f"{self.__quellordner[index]}\\{neuer_dateiname}")
            self.zielordner_durchlaufen_und_einsortieren()
