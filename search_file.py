import os
import platform
import pefile

def get_file(nom_fichier):

    if platform.system() == "Windows":
        repertoire = "C:\\"
    elif platform.system() == "Linux":
        repertoire = "/"
    else:
        raise Exception("Système d'exploitation non supporté")
    
    for dossier, _, fichiers in os.walk(repertoire):
        if nom_fichier in fichiers:
            return os.path.join(dossier, nom_fichier)
    return None
