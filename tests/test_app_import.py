def test_app_import():
    import importlib
    mod = importlib.import_module('app')
    assert hasattr(mod, 'app')
    from flask import Flask
    assert isinstance(mod.app, Flask)
