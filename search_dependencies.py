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

# PARTI CISCO
def get_dependencies_windows(dll_path, seen=None):
    if seen is None:
        seen = set()
    dependencies = set()
    try:
        pe = ctypes.windll.pe.GetModuleHandleW(dll_path)
        buffer = ctypes.create_unicode_buffer(1024)
        ctypes.windll.kernel32.GetModuleFileNameW(pe, buffer, ctypes.sizeof(buffer))
        dependencies.add(buffer.value)
        for entry in range(0, ctypes.windll.kernel32.DllMain(pe, 0, 0), 0):
            buffer = ctypes.create_unicode_buffer(1024)
            ctypes.windll.kernel32.GetModuleFileNameW(entry, buffer, ctypes.sizeof(buffer))
            dependency = buffer.value
            if dependency not in seen:
                seen.add(dependency)
                dependencies.update(get_dependencies_windows(dependency, seen))
    except Exception as e:
        print("Error:", e)
    return dependencies
