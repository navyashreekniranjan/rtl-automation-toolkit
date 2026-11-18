import re

def analyze_ports(rtl_file):
    
    
    with open(rtl_file, "r") as file:
        content = file.read()
    ports = []
    match = re.search(
        r"module\s+\w+\s*\((.*?)\)\s*;",
        content,
        re.DOTALL
        )

    if match:
        port_list = match.group(1)

        port_declaration = port_list.split(",")

        current_direction = None
        current_range = None

        for port in port_declaration:
            parts = re.findall(r"\w+|\[\d+:\d+\]",port)

            if not parts:
                continue

            if parts[0] in ["input", "output", "inout"]:
                current_direction = parts[0]
                current_range = None

            direction = current_direction
            name = parts[-1]

            range_match = re.search(r"\[(\d+):(\d+)\]", port)

            if range_match:
                current_range = (
                    int(range_match.group(1)),
                    int(range_match.group(2))
                )
            
            if current_range is not None:
                msb,lsb = current_range
                width = abs(msb -lsb) + 1
            else:
                width = 1

            port_info = {
                "name": name,
                "direction": direction,
                "width": width
                }

            ports.append(port_info)

    return ports




if __name__ == "__main__":
    result = analyze_ports("rtl/ports_example.v")

    print("Total Ports: ", len(result))

    for port in result:
        print(port)


    
