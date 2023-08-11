class Conf:
    def __init__(self, pfad):
        self.__pfad = pfad

    def auswahl_einstellungen(self):
        print("Was möchtest du tun?")
        print("1 - Neuer Quellordner anlegen")
        print("2 - Neuer Zielordner anlegen")
        auswahl = input("Deine Wahl: ")


    def conf_erstellen(self):
        ...