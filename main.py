from recursif_dependencies import *

LIB_BASE = "LibPlants.so"
extension = LIB_BASE.find('.dll')
all_dependencies = {}

if extension >= 1:
    process_dependencies_windows(LIB_BASE, all_dependencies)
else:
    process_dependencies_linux(LIB_BASE, all_dependencies)

for file_path, dependency in all_dependencies.items():
    print(f"{dependency} -> {file_path}")

