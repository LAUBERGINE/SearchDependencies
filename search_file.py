import os

def get_file(nom_fichier):
    repertoire="/"
    for dossier, sous_repertoires, fichiers in os.walk(repertoire):
        if nom_fichier in fichiers:
            return os.path.join(dossier, nom_fichier)
    return None