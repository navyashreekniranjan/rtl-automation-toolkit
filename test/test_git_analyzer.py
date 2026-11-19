from rtl_toolkit.git_manager.git_analyzer import get_git_status

def test_get_git_status_returns_all_categories():
    changes = get_git_status()
    assert set(changes.keys()) == {
        "added",
        "modified",
        "deleted",
        "untracked"
    }

def test_untracked_file_detection():
    changes = get_git_status()

    assert "rtl_toolkit/git_manager/" in changes["untracked"]