import subprocess


def get_git_status():
    command = ["git", "status", "--short"]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError("Git status command failed: " + result.stderr)

    changes = {
        "added": [],
        "modified": [],
        "deleted": [],
        "untracked": []
    }

    for line in result.stdout.splitlines():
        status = line[:2]
        filepath = line[3:]
        index_status = status[0]
        working_status = status[1]

        if status == "??":
            changes["untracked"].append(filepath)
        elif "D" in index_status or "D" in working_status:
            changes["deleted"].append(filepath)
        elif "A" in index_status or "A" in working_status:
            changes["added"].append(filepath)
        elif "M" in index_status or "M" in working_status:
            changes["modified"].append(filepath)
    return changes