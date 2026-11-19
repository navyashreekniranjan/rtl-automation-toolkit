from rtl_toolkit.reports.csv_report import generate_csv_report
import csv


def test_generate_csv_report(tmp_path):
    report_data = [
        {"module_name": "counter", "port_count": 3, "status": "PASS"},
        {"module_name": "adder", "port_count": 4, "status": "PASS"}
    ]

    output_file = tmp_path / "rtl_report.csv"

    generate_csv_report(report_data, output_file)

    assert output_file.exists()

    with open(output_file, "r", newline="") as file:
        saved_data = list(csv.DictReader(file))

    assert saved_data == [
        {"module_name": "counter", "port_count": "3", "status": "PASS"},
        {"module_name": "adder", "port_count": "4", "status": "PASS"}
    ]