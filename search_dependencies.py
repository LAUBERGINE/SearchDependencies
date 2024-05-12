
import ctypes
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
import ctypes.wintypes as wintypes

def get_dependencies_windows(dll_path):
    # Function to get list of modules loaded by a DLL
    def list_loaded_modules(dll_path):
        hModule = ctypes.WinDLL(dll_path)
        hProcess = ctypes.windll.kernel32.GetCurrentProcess()
        modules = (wintypes.HMODULE * 256)()
        needed = wintypes.DWORD()
        ctypes.windll.psapi.EnumProcessModules(hProcess, ctypes.byref(modules), ctypes.sizeof(modules), ctypes.byref(needed))
        num_modules = needed.value // wintypes.DWORD(ctypes.sizeof(wintypes.HMODULE)).value
        module_names = set()
        for i in range(num_modules):
            baseName = (ctypes.c_char * 1024)()
            ctypes.windll.psapi.GetModuleBaseNameA(hProcess, modules[i], baseName, 1024)
            module_names.add(baseName.value.decode('utf-8'))
        return module_names

    try:
        return list_loaded_modules(dll_path)
    except Exception as e:
        print("Error loading modules from DLL:", e)
        return set()

