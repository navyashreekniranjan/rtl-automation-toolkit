import re

def analyze_parameters(rtl_file):
    with open(rtl_file, "r") as file:
        contents = file.read()

    parameters = []

    pattern = r"\bparameter\s+([^;)]+)"
    matches = re.findall(pattern,contents)
    

    for declaration in matches:
        parts = declaration.split(",")
        
        for part in parts:
            part = part.strip()

            part = re.sub(r"^parameter\s+", "", part)

            if "=" not in part:
                continue

            name, value = part.split("=", 1)

            parameter_info = {
                "name": name.strip(),
                "value": value.strip()
            }

            parameters.append(parameter_info)

    return parameters