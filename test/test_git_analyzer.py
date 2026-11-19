from rtl_toolkit.git_manager.git_analyzer import get_git_status
import subprocess

def test_get_git_status_returns_all_categories():
    changes = get_git_status()
    
    assert set(changes.keys()) == {
        "added",
        "modified",
        "deleted",
        "untracked"
    }

def test_untracked_file_detection(monkeypatch):
    def mock_run(*args, **kwargs):
        return subprocess.CompletedProcess(
                args=args,
                returncode=0,
                stdout="?? rtl_toolkit/new_file.py\n",
                stderr=""
            )
    
    monkeypatch.setattr(subprocess, "run", mock_run)
    
    changes = get_git_status()

    assert "rtl_toolkit/new_file.py" in changes["untracked"]