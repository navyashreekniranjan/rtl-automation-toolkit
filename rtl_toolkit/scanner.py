from pathlib import Path

def find_rtl_files(rtl_directory):
    rtl_directory = Path(rtl_directory)

    if not rtl_directory.exists():
        raise FileNotFoundError(
            f"RTL directory does not exist: {rtl_directory}"
        )

    if not rtl_directory.is_dir():
        raise NotADirectoryError(
            f"Path is not a directory: {rtl_directory}"
        )

    rtl_files = []

    for file in rtl_directory.rglob("*"):
        if file.is_file() and file.suffix in [".v", ".sv"]:
            rtl_files.append(file)

    return rtl_files



if __name__ == "__main__":
    files = find_rtl_files("rtl")

    print("RTL files found: ")

    for file in files:
        print(file)

    print("total files: ",len(files))       