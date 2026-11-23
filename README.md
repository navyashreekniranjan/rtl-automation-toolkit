## RTL AUTOMATION TOOLKIT

A Python-based automation toolkit for analyzing Verilog RTL designs, detecting potential issues, running lint checks, analyzing Git changes, and generating reports.


## Features

- RTL File Scanner : Finds RTL source files in the project
- Module Analyzer : Identifies module declaration
- Port Analyzer: Extracts module ports, supporting ANSI and non-ANSI declarations.
- Parameter Analyzer: Extracts module parameters.
- Duplicate Checker: Detects duplicate module definitions.
- Dependency Analyzer: Identifies module dependencies.
- Verilator Integration: Runs lint checks on RTL files.
- Git Analyzer: Checks Git repository status and file changes.
- Report Generation: Generates JSON, CSV, and HTML reports.


## Technologies used
- Python3
- Regular expressions
- Verilator
- Git
- Pytest


## Project Structure
```text
rtl-automation-toolkit/
├── main.py
├── generate_sample_report.py
├── requirements-dev.txt
├── README.md
├── .gitignore
├── rtl/
├── rtl_toolkit/
│   ├── module_analyzer.py
│   ├── parameter_analyzer.py
│   ├── duplicate_checker.py
│   ├── dependency_analyzer.py
│   ├── lint/
│   ├── git_manager/
│   └── reports/
├── test/
└── reports/
```

## Installation

- Clone the repository:
    git clone https://github.com/navyashreekniranjan/rtl-automation-toolkit.git
- Navigate into the project directory:
    cd rtl-automation-toolkit
- Install development dependencies:
    pip install -r requirements-dev.txt
- Ensure Python 3, Git, and Verilator are installed and available in your system PATH.

```bash
git clone https://github.com/navyashreekniranjan/rtl-automation-toolkit.git
cd rtl-automation-toolkit
pip install -r requirements-dev.txt
```


## Usage

- Run the toolkit from the project root:
    python main.py
- The toolkit analyzes the RTL files and generates reports in the reports/ directory.


## Running Tests

- Run the automated test suite:
    python -m pytest -v


## Known Limitations

- Some RTL constructs may not be fully recognized by the current regular-expression-based       
  analyzers.
- Dependency analysis may report false positives for certain Verilog keywords.
- Verilator lint results depend on the syntax and validity of the input RTL files.


## Future Improvements

- Improve RTL parsing to support more Verilog and SystemVerilog constructs.
- Reduce false positives in dependency analysis.
- Expand automated test coverage.
- Add more detailed lint and analysis reports.

## Author

**Navyashree K N**
- GitHub: https://github.com/navyashreekniranjan/rtl-automation-toolkit.git
