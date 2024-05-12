from search_dependencies import get_dependencies_linux, get_dependencies_windows
from search_file import get_file

def process_dependencies_linux(file_path, all_dependencies):
    dependencies = get_dependencies_linux(file_path)
    dependencies_list = list(dependencies)
    for dependency in dependencies_list:
        result = get_file(dependency)
        if result:
            all_dependencies[result] = file_path 
            process_dependencies_linux(result, all_dependencies)
        else:
            all_dependencies[dependency] = file_path 

# PARTIE WINDOWS

def process_dependencies_windows(file_path, all_dependencies):
    dependencies = get_dependencies_windows(file_path)
    dependencies_list = list(dependencies)
    for dependency in dependencies_list:
        result = get_file(dependency)
        if result:
            all_dependencies[result] = file_path
            process_dependencies_windows(result, all_dependencies)
        else:
            all_dependencies[dependency] = file_path
