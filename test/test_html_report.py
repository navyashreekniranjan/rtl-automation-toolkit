from rtl_toolkit.reports.html_report import generate_html_report


def test_generate_html_report(tmp_path):
    report_data = [
        {"module_name": "counter", "port_count": 3, "status": "PASS"},
        {"module_name": "adder", "port_count": 4, "status": "PASS"}
    ]

    output_file = tmp_path / "rtl/report.html"

    generate_html_report(report_data, output_file)

    assert output_file.exists()

    with open(output_file, "r") as file:
        content = file.read()

    assert "RTL Automation Report" in content
    assert "counter" in content
    assert "adder" in content
