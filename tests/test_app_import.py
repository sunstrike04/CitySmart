def test_app_import():
    # Load app.py directly from the repo so CI doesn't fail on import paths.
    import importlib.util
    from pathlib import Path

    repo_root = Path(__file__).resolve().parent.parent
    app_path = repo_root / 'app.py'

    spec = importlib.util.spec_from_file_location('app', str(app_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert hasattr(mod, 'app')
    from flask import Flask
    assert isinstance(mod.app, Flask)
