"""Test for assertion module."""
# official library
import pytest

# my modules
from storybuilder.util.assertion import is_int, is_str


@pytest.mark.parametrize("x",
        [1, 0, -1,])
def test_assertion_is_int(x):

    assert is_int(x) or is_int(x) == 0, f"Expected an integer type value: {x}"


@pytest.mark.parametrize("x",
        ["a", [1,2,3], {"a":1,},])
def test_assertion_is_int__failure(x):

    with pytest.raises(AssertionError):
        is_int(x)

@pytest.mark.parametrize("x",
        ["a", "日本語",
            """Multi
               Line
            """])
def test_assertion_is_str(x):

    assert is_str(x), f"Expected a string type value: {x}"


@pytest.mark.parametrize("x",
        [1, [], {}])
def test_assertion_is_str__failure(x):

    with pytest.raises(AssertionError):
        is_str(x)
