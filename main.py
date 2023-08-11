from Conf import *


print(f"Hi schön das du da bist")
print(f"Was möchtest du tun?")
print(f"1 - Dateien einsortieren")
print(f"2 - Einstellungen")
auswahl = input("Deine Wahl: ")

if auswahl == "1":
    #TODO
    print("Dateien wurden Einsortiert")
elif auswahl == "2":
    conf = Conf()
    conf.auswahl_einstellungen()














# import shutil, os
#
# # Quellordner
# source = r"C:\Users\aless\Downloads\Schule"
#
# # Zielordner
# bsL = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\BS\BS-L"
# bsW = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\BS\BS-W"
# bew = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\BEW"
# ctKts = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\CT.KTS"
# db = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\DB"
# dbk = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\DBK"
# rew = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\REW"
# itsi = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\ITSI"
# java = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\JAVA"
# lo = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\LO"
# web = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\WEB"
# eng = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\ENG"
# etec = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\ETEC"
# ebus = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\EBUS"
# swt = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\SWT"
# net = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\NET"
# wiso = r"C:\Users\aless\OneDrive\Dokumente\SRH\FIA1\WISO"
# algemein = r"C:\Users\aless\OneDrive\Dokumente\SRH\Allgemein"
#
# dic_feacher = {"BS-L": bsL, "BS-W": bsW, "BEW": bew,
#                "CT.KTS": ctKts, "DB": db, "ETEC": etec,
#                "REW": rew, "DBK": dbk, "ITSI": itsi,
#                "JAVA": java, "LO": lo, "WEB": web,
#                "ENG": eng, "SWT": swt, "NET": net,
#                "WISO": wiso, "ALLGEMEIN": algemein,
#                "EBUS": ebus}
#
# # Dateinamen
# # Datum_Fach_Quelle_Inhalt.pdf
# # Quellen
# # präsentation - pr
# # bild -> bi
# # onenote -> on
# # moodle -> mo
# # inet -> in !!! zusatz Infos -> in
# # papier -> pa
# # zusammenfasung -> zu -> kl
# # mindmap -> mi -> kl
# # klausur -> kl
#
#
# def fachwahl(fach="", pfad=""):
#     try:
#         if datei_split[1].upper() == fach: # Fach abfragen
#             if datei_split[2].upper() == "ON":
#                 shutil.move(source + "\\" + datei, pfad + "\\" + "OneNote" + "\\" + datei)
#             elif datei_split[2].upper() == "MO":
#                 shutil.move(source + "\\" + datei, pfad + "\\" + "Moodle" + "\\" + datei)
#             elif datei_split[2].upper() == "IN":
#                 shutil.move(source + "\\" + datei, pfad + "\\" + "Inetinfo" + "\\" + datei)
#             elif datei_split[2].upper() == "PA":
#                 shutil.move(source + "\\" + datei, pfad + "\\" + "Papier" + "\\" + datei)
#             elif datei_split[2].upper() in ("ZU", "MI", "KL"):
#                 shutil.move(source + "\\" + datei, pfad + "\\" + "Klausur" + "\\" + datei)
#             elif datei_split[2].upper() == "BI":
#                 shutil.move(source + "\\" + datei, pfad + "\\" + "Bilder" + "\\" + datei)
#             elif datei_split[2].upper() == "PR":
#                 shutil.move(source + "\\" + datei, pfad + "\\" + "Präsentation" + "\\" + datei)
#             else:
#                 shutil.move(source + "\\" + datei, pfad + "\\" + datei)
#
#     except FileNotFoundError:
#         print("Error")
#         print(datei)
#         input("Weiter mit Enter")
#
#
# files = os.listdir(source)
# for datei in files:
#     try:
#         datei_split = datei.split("_")
#         for f, p in dic_feacher.items():
#             fachwahl(fach=f, pfad=p)
#     except IndexError:
#         print("Fehlerhafter Dateiname")
#         print(datei)
#         x = input("Weiter mit Enter")
