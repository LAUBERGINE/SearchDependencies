from recursif_dependencies import process_dependencies_linux, process_dependencies_windows
from search_file import get_file

LIB_BASE = "LibPlants.so"
ROOT_LIB_BASE = get_file(LIB_BASE)
extension = LIB_BASE.find('.dll')
all_dependencies = {}

if extension >= 1:
    process_dependencies_windows(ROOT_LIB_BASE, all_dependencies)
else:
    process_dependencies_linux(ROOT_LIB_BASE, all_dependencies)

for file_path, dependency in all_dependencies.items():
    print(f"{dependency} -> {file_path}")

