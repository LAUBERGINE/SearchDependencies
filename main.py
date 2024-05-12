
from recursif_dependencies import process_dependencies_linux, process_dependencies_windows
from search_file import get_file

# Constantes
LIB_BASE = "user32.dll"
WINDOWS_EXTENSION = '.dll'

# Fonction pour déterminer le système d'exploitation en fonction de l'extension du fichier
def determine_os(file_path):
    if file_path.endswith(WINDOWS_EXTENSION):
        return 'Windows'
    else:
        return 'Linux'

try:
    # Obtention du chemin absolu du fichier racine
    ROOT_LIB_BASE = get_file(LIB_BASE)

    # Sélection du système d'exploitation en fonction de l'extension du fichier racine
    os_type = determine_os(ROOT_LIB_BASE)

    # Traitement des dépendances en fonction du système d'exploitation
    all_dependencies = {}
    if os_type == 'Windows':
        process_dependencies_windows(ROOT_LIB_BASE, all_dependencies)
    else:
        process_dependencies_linux(ROOT_LIB_BASE, all_dependencies)

    # Affichage des dépendances
    print(f"Dependencies for {LIB_BASE} (OS: {os_type}):")
    for dependency, file_path in all_dependencies.items():
        print(f"\t{file_path} -> {dependency}")

except Exception as e:
    print(f"Error occurred: {str(e)}")
