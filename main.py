from rtl_toolkit.scanner import find_rtl_files
from rtl_toolkit.port_analyzer import analyze_ports
from rtl_toolkit.module_analyzer import extract_modules
from rtl_toolkit.parameter_analyzer import analyze_parameters
from rtl_toolkit.duplicate_checker import duplicate_checker
from rtl_toolkit.dependency_analyzer import analyze_dependencies

from rtl_toolkit.lint.verilator_runner import run_verilator
from rtl_toolkit.git_manager.git_analyzer import get_git_status

from rtl_toolkit.reports.json_report import generate_json_report
from rtl_toolkit.reports.csv_report import generate_csv_report
from rtl_toolkit.reports.html_report import generate_html_report

def main():

    rtl_files = find_rtl_files("rtl")
    print("rtl files Found:")
    for rtl_file in rtl_files:
        print(rtl_file)

    print("\nModule Analysis:")
    for rtl_file in rtl_files:
        modules = extract_modules(rtl_file)
        print(rtl_file, ":", modules)

    print("\nPort Analysis:")
    for rtl_file in rtl_files:
        ports = analyze_ports(rtl_file)
        print(rtl_file , ":", ports)

    print("\nParameter Analysis:")
    for rtl_file in rtl_files:
        parameters = analyze_parameters(rtl_file)
        print(rtl_file, ":", parameters)

    print("\nDuplicate Module Analysis:")    
    duplicates = duplicate_checker(rtl_files)
    print("Duplicate Modules:", duplicates)

    print("\nDependency Analysis:")
    dependencies = analyze_dependencies(rtl_files)
    print("Dependencies:", dependencies)

    print("\nVerilator Lint Analysis:")
    lint_results = {}
    for rtl_file in rtl_files:
        lint_result = run_verilator(str(rtl_file))
        lint_results[rtl_file] = lint_result
        print(rtl_file , ":", lint_result["status"])

    print("\nGit Status Integration:")
    git_changes = get_git_status()
    print("Git changes:", git_changes)

    print("\nReport Data Preparation:")
    report_data = []
    for rtl_file in rtl_files:
        modules = extract_modules(rtl_file)
        lint_result = lint_results[rtl_file]
        
        for module_name in modules:
            ports = analyze_ports(rtl_file, module_name)
            module_report = {
                "module_name": module_name,
                "port_count": len(ports),
                "status": lint_result["status"]
            }
            report_data.append(module_report)
    print("Report Data:", report_data)

    print("\nJSON Report:")
    json_file = generate_json_report(
        report_data,
        "reports/rtl_report.json")
    print("JSON Report Generated:", json_file)

    print("\nCSV Report:")
    csv_file = generate_csv_report(
        report_data,
        "reports/rtl_report.csv")
    print("CSV Report Generated:", csv_file)

    print("\nHTML Report:")
    html_report = generate_html_report(
        report_data,
        "reports/rtl_report.html")
    print("HTML Report Generated:", html_report)

   




if __name__ == "__main__":
    main()
