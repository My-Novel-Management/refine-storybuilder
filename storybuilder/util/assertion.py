"""Utility module for assertion."""


__all__ = (
        'is_int',
        'is_str',
        )


def is_int(val: int) -> int:
    """Assertion for an integer type value.

    Args:
        val: check value (expect int type)

    Returns:
        Same value to input.

    Raises:
        Assertion Error: if a value not match an integer type.
    """
    assert isinstance(val, int), f"Must be a Integer type value!: {type(val)}"
    return val


def is_str(val: str) -> str:
    """Assertion for a string type value.

    Args:
        val: check value (expect string type)

    Returns:
        Same value to input.

    Raises:
        Assertion Error: if a value not match a string type.
    """
    assert isinstance(val, str), f"Must be a String type value!: {type(val)}"
    return val
