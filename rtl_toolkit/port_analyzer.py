
import re


def analyze_ports(rtl_file, module_name=None):
    with open(rtl_file, "r") as file:
        content = file.read()

    ports = []

    # Find module declarations and their port lists.
    module_pattern = re.compile(
        r"\bmodule\s+(\w+)\s*\((.*?)\)\s*;(.*?)\bendmodule",
        re.DOTALL
    )

    for match in module_pattern.finditer(content):
        found_module_name = match.group(1)
        port_list = match.group(2)
        module_body = match.group(3)

        # Analyze only the requested module, if specified.
        if module_name is not None and found_module_name != module_name:
            continue

        current_direction = None
        current_range = None

        # Handle ANSI-style declarations.
        port_declarations = port_list.split(",")

        for port in port_declarations:
            parts = re.findall(r"\w+|\[\d+:\d+\]", port)

            if not parts:
                continue

            if parts[0] in ["input", "output", "inout"]:
                current_direction = parts[0]
                current_range = None

            name = parts[-1]

            range_match = re.search(r"\[(\d+):(\d+)\]", port)

            if range_match:
                current_range = (
                    int(range_match.group(1)),
                    int(range_match.group(2))
                )

            if current_range is not None:
                msb, lsb = current_range
                width = abs(msb - lsb) + 1
            else:
                width = 1

            ports.append({
                "name": name,
                "direction": current_direction,
                "width": width
            })

        # Handle non-ANSI-style declarations.
        if ports and all(port["direction"] is None for port in ports):
            ports.clear()

        if not ports:
            port_names = [
                name.strip()
                for name in port_list.split(",")
                if name.strip()
            ]

            for declaration in re.finditer(
                r"\b(input|output|inout)\s*"
                r"(?:reg\s*|wire\s*|logic\s*)?"
                r"(?:\[(\d+):(\d+)\]\s*)?"
                r"([^;]+);",
                module_body
            ):
                direction = declaration.group(1)

                if declaration.group(2) is not None:
                    msb = int(declaration.group(2))
                    lsb = int(declaration.group(3))
                    width = abs(msb - lsb) + 1
                else:
                    width = 1

                declared_names = declaration.group(4).split(",")

                for declared_name in declared_names:
                    name = declared_name.strip()

                    if name in port_names:
                        ports.append({
                            "name": name,
                            "direction": direction,
                            "width": width
                        })

        if module_name is None or found_module_name == module_name:
            return ports

    return ports


if __name__ == "__main__":
    result = analyze_ports("rtl/counter.v", "counter")

    print("Total Ports:", len(result))

    for port in result:
        print(port)

