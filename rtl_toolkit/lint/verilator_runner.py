import subprocess


def run_verilator(rtl_file):
    command = ["verilator", "--lint-only", "-Wall", rtl_file]
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        return {
        "status": "TOOL_ERROR",
        "returncode": None,
        "stdout": "",
        "stderr": "Verilator is not installed or not available in PATH."
    }

    if result.returncode == 0:
        status = "PASS"
    else:
        status = "FAIL"
    return{
        "status": status,
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }

if __name__ == "__main__":
    result = run_verilator("rtl/invalid_example.v")
    if result is not None:
        print("Lint Status:", result["status"])
        print("RTL Files:", "rtl/invalid_example.v")
        print("Return code: ", result["returncode"])
        print("stdout: ", result["stdout"])
        print("stderr: ", result["stderr"])
        