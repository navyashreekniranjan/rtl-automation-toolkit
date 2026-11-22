from rtl_toolkit.reports.html_report import generate_html_report

report_data = [
    {"module_name": "counter", "port_count": 3, "status": "PASS"},
    {"module_name": "adder", "port_count": 4, "status": "PASS"}
]

output_file =  generate_html_report(
    report_data,
    "reports/rtl_report.html"
)

print("HTML report generated:", output_file)
