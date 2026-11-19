import csv


def generate_csv_report(report_data, output_file):
    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["module_name", "port_count", "status"]
        )
        writer.writeheader()
        writer.writerows(report_data)

    return output_file