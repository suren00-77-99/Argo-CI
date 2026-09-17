from pathlib import Path


def test_backend_source_exists():
    app_file = Path(__file__).resolve().parents[1] / "app.py"

    assert app_file.exists()