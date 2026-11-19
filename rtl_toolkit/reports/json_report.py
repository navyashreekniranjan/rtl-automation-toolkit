import json
from pathlib import Path


def generate_json_report(report_data, output_file):
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w") as file:
        json.dump(report_data, file, indent=4)
    
    return output_file