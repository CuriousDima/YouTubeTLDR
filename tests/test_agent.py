"""Basic tests for the YouTubeTLDR agent."""

import pytest
from agent import main, __version__


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_main(capsys):
    """Test main function runs without error."""
    main()
    captured = capsys.readouterr()
    assert "YouTube TLDR Agent" in captured.out
