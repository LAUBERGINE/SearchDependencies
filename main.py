from recursif_dependencies import *

LIB_BASE = "LibPlants.so"
index_point = LIB_BASE.find('.')
if index_point != -1:
    apres_point = LIB_BASE[index_point + 1:]
all_dependencies = {}

if apres_point == "dll":
    process_dependencies_windows(LIB_BASE, all_dependencies)
else:
    process_dependencies_linux(LIB_BASE, all_dependencies)

for file_path, dependency in all_dependencies.items():
    print(f"{dependency} -> {file_path}")

