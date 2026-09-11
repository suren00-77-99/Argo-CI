def test_frontend_source_exists():
    from pathlib import Path
    assert Path("frontend/app.py").exists()
