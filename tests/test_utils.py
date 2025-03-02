"""
🔍 Test Utilities – Archivyx
"""

from archivyx.utils import format_output

def test_format_output():
    """Test text formatting function"""
    result = format_output("Hello World")
    assert isinstance(result, str)  # Should return a string
    assert "Hello World" in result  # Should contain input text
