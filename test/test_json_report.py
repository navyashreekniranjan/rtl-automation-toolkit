from rtl_toolkit.reports.json_report import generate_json_report
import json


def test_generate_json_report(tmp_path):
    report_data = {
        "module_name": "counter",
        "port_count":3
    }

    output_file = tmp_path / "rtl/report.json"

    generate_json_report(report_data, output_file) 

    assert output_file.exists()

    with open(output_file, "r") as file:
        saved_data = json.load(file)

        assert saved_data == report_data