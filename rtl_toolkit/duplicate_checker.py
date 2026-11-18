from .module_analyzer import extract_modules

def duplicate_checker(rtl_files):
    module_files = {}

    for rtl_file in rtl_files:
        module_names = extract_modules(rtl_file)

        for module_name in module_names:
            if module_name not in module_files:
                module_files[module_name]= []

            module_files[module_name].append(str(rtl_file))

    duplicates = {}
    for module_name, files in module_files.items():
        if len(files) > 1:
            duplicates[module_name] = files
    return duplicates 