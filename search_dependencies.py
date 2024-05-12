import pefile
import subprocess

def get_dependencies_linux(so_path):
    try:
        result = subprocess.run(["objdump", "-p", so_path], capture_output=True, text=True)
        lines = result.stdout.split('\n')
        dependencies = set()
        for line in lines:
            if "NEEDED" in line:
                dependency = line.split()[1]
                dependencies.add(dependency)
        return dependencies
    except Exception as e:
        print("Error:", e)
        return None

# PARTIE WINDOWS

def get_dependencies_windows(dll_path):
    dependencies = set()
    pe = pefile.PE(dll_path)
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        dependencies.add(entry.dll.decode('utf-8'))
    return dependencies
