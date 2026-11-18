import re
from pathlib import Path
from .scanner import find_rtl_files

def extract_modules(rtl_file):
    rtl_file = Path(rtl_file)

    with open(rtl_file, "r") as file:
        contents = file.read()

    contents = re.sub(r"//.*|/\*[\s\S]*?\*/", "", contents)

    pattern = r"\bmodule\s+(\w+)" 

    modules = re.findall(pattern, contents)

    return modules






if __name__ == "__main__":
    rtl_files = find_rtl_files("rtl")

    for rtl_file in rtl_files:
        modules = extract_modules(rtl_file)

        print("File: ", rtl_file)
        print("Modules:", modules)
        print("------------------------")