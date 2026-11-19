from pathlib import Path
import html

def generate_html_report(report_data, output_file):
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>RTL Automation Report</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 30px;
                background-color: #f4f4f4;
            }

            h1 {
                text-align: center;
            }

            table {
                border-collapse: collapse;
                width: 100%;
                background-color: white;
            }

            th, td {
                border: 1px solid #cccccc;
                padding: 10px;
                text-align: left;
            }

            th {
                background-color: #333333;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>RTL Automation Report</h1>
        <table>
            <tr>
                <th>Module Name</th>
                <th>Port Count</th>
                <th>Status</th>
            </tr>
    """

    for module in report_data:
        module_name = module["module_name"]
        port_count = module["port_count"]
        status = module["status"]

        module_name = html.escape(str(module_name))
        port_count = html.escape(str(port_count))
        status = html.escape(str(status))

        html_content += f"""
            <tr>
                <td>{module_name}</td>
                <td>{port_count}</td>
                <td>{status}</td>
            </tr>
        """
    html_content += """
            </table>
        </body>
        </html>
    """

    with open(output_file, "w") as file:
        file.write(html_content)

    return output_file