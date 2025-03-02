"""
🔍 Test CLI Prompts – Archivyx
"""


from archivyx.prompts import vert_prompt, hori_prompt

def test_vert_prompt(monkeypatch):
    """Test vertical prompt selection"""
    monkeypatch.setattr("keyboard.read_event", lambda: type("", (), {"name": "enter"})())  # Simulate Enter key
    options = ["Option 1", "Option 2", "Option 3"]
    selected = vert_prompt(options, "Choose:")
    assert selected in options  # Ensure the output is one of the options

def test_hori_prompt(monkeypatch):
    """Test horizontal prompt selection"""
    monkeypatch.setattr("keyboard.read_event", lambda: type("", (), {"name": "enter"})())  # Simulate Enter key
    options = ["Yes", "No"]
    selected = hori_prompt(options, "Continue?")
    assert selected in options  # Ensure the output is one of the options
