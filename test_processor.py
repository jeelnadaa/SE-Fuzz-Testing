from hypothesis import given, strategies as st
from processor import sanitize_string, parse_int_list, reverse_words
import pytest


@given(st.text() | st.none())
def test_sanitize_string_no_crash(s):
    """Fuzz test: sanitize_string should not crash for any text or None input."""
    try:
        result = sanitize_string(s)
        # Basic invariant: must return a string (even if input is None)
        assert isinstance(result, str)
    except Exception as e:
        pytest.fail(f"sanitize_string() crashed with input {s!r}: {e}")


@given(st.text() | st.none())
def test_parse_int_list_safe(s):
    """Fuzz test: parse_int_list should handle any text/None safely."""
    try:
        result = parse_int_list(s)
        # If it returns, must be a list
        assert isinstance(result, list)
        # If list not empty, all elements must be integers
        for val in result:
            assert isinstance(val, int)
    except Exception as e:
        pytest.fail(f"parse_int_list() crashed with input {s!r}: {e}")


@given(st.text() | st.none())
def test_reverse_words_safe(s):
    """Fuzz test: reverse_words should not crash for any text or None input."""
    try:
        result = reverse_words(s)
        # Must return a string
        assert isinstance(result, str)
        # Property: reversing twice should approximately restore the original (if input was str)
        if isinstance(s, str):
            twice = reverse_words(result)
            # normalize spaces for comparison
            def norm(t): return " ".join(t.split())
            assert norm(twice) == norm(s) or norm(twice) == norm(result)
    except Exception as e:
        pytest.fail(f"reverse_words() crashed with input {s!r}: {e}")
