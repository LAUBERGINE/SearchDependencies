import os
import platform
import pefile

def find_first_three_library_files(start_directory, file_extension):
    library_files = []
    for folder, _, files in os.walk(start_directory):
        for file in files:
            if file.endswith(file_extension):
                library_files.append(os.path.join(folder, file))
                if len(library_files) == 10:
                    return library_files
    return library_files

def list_dll_dependencies(dll_path):
    try:
        pe = pefile.PE(dll_path)
        dependencies = []
        if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                dep_name = entry.dll.decode('utf-8')
                if dep_name != os.path.basename(dll_path):
                    dependencies.append(dep_name)
        else:
            dependencies.append("No dependencies found")
        return dependencies
    except Exception as e:
        return [f"Error processing {dll_path}: {str(e)}"]

if platform.system() == "Windows":
    start_directory = "C:\\Windows\\System32"
    file_extension = ".dll"
elif platform.system() == "Linux":
    start_directory = "/usr/lib"
    file_extension = ".so"
else:
    raise Exception("Unsupported OS")

library_files = find_first_three_library_files(start_directory, file_extension)
for library_file in library_files:
    print(f"Found Library File: {library_file}")
    dependencies = list_dll_dependencies(library_file)
    print(f"Dependencies for {library_file}:")
    if not dependencies:
        print("  No dependencies or error reading dependencies.")
    else:
        for dep in dependencies:
            print(f"  {dep}")
