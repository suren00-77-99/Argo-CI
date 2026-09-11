def test_backend_source_exists():
    from pathlib import Path
    assert Path("backend/app.py").exists()
