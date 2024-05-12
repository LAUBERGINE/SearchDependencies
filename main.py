from recursif_dependencies import process_dependencies_linux, process_dependencies_windows
from search_file import get_file
import platform

LIB_BASE = "office.dll"


ROOT_LIB_BASE = get_file(LIB_BASE)
all_dependencies = {}

if platform.system() == "Windows":
    process_dependencies_windows(ROOT_LIB_BASE, all_dependencies)

else:
    process_dependencies_linux(ROOT_LIB_BASE, all_dependencies)

print(f"Dependencies for {LIB_BASE} :")
for dependency, file_path in all_dependencies.items():
    print(f"\t{file_path} -> {dependency}")