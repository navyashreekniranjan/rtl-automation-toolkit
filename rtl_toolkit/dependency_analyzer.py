import re
from .module_analyzer import extract_modules


def analyze_dependencies(rtl_files):
    dependencies = {}
    defined_modules = set()

    for rtl_file in rtl_files:
        module_names = extract_modules(rtl_file)

        for module_name in module_names:
            dependencies.setdefault(module_name, [])
        defined_modules.update(module_names)

        with open(rtl_file, "r") as file:
            content = file.read()

            pattern = r"\b(\w+)\s+(\w+)\s*\("
            module_pattern = r"\bmodule\s+(\w+)\b(.*?)\bendmodule\b"
            module_matches = re.findall(module_pattern, content, re.DOTALL)

            for parent_module, module_body in module_matches:
                matches = re.findall(pattern, module_body)

                for module_type, instance_name in matches:
                    dependencies[parent_module].append(module_type)

    instantiated_modules = set()
    for child_modules in dependencies.values():
        instantiated_modules.update(child_modules)

    unresolved_modules = instantiated_modules - defined_modules
    
    return {
        "dependencies": dependencies,
        "unresolved_modules": sorted(unresolved_modules)
    }
