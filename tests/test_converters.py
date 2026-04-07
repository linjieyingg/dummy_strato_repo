import pytest
from src.converters import binary_to_decimal

def test_binary_to_decimal_valid_inputs():
    """
    Tests binary_to_decimal with various valid binary strings.
    """
    assert binary_to_decimal("0") == 0
    assert binary_to_decimal("1") == 1
    assert binary_to_decimal("10") == 2
    assert binary_to_decimal("11") == 3
    assert binary_to_decimal("100") == 4
    assert binary_to_decimal("101") == 5
    assert binary_to_decimal("111") == 7
    assert binary_to_decimal("1000") == 8
    assert binary_to_decimal("101010") == 42
    assert binary_to_decimal("11111111") == 255
    assert binary_to_decimal("100000000000000000000000000000000000000000000000000000000000000") == 2**62

def test_binary_to_decimal_leading_zeros():
    """
    Tests binary_to_decimal with binary strings containing leading zeros.
    """
    assert binary_to_decimal("00") == 0
    assert binary_to_decimal("01") == 1
    assert binary_to_decimal("0010") == 2
    assert binary_to_decimal("000000000101") == 5

def test_binary_to_decimal_invalid_type():
    """
    Tests binary_to_decimal with non-string inputs, expecting TypeError.
    """
    with pytest.raises(TypeError, match="Input must be a string."):
        binary_to_decimal(101)
    with pytest.raises(TypeError, match="Input must be a string."):
        binary_to_decimal(None)
    with pytest.raises(TypeError, match="Input must be a string."):
        binary_to_decimal(['1', '0', '1'])
    with pytest.raises(TypeError, match="Input must be a string."):
        binary_to_decimal(True)

def test_binary_to_decimal_empty_string():
    """
    Tests binary_to_decimal with an empty string, expecting ValueError.
    """
    with pytest.raises(ValueError, match="Input string cannot be empty."):
        binary_to_decimal("")

def test_binary_to_decimal_invalid_characters():
    """
    Tests binary_to_decimal with strings containing non-binary characters, expecting ValueError.
    """
    with pytest.raises(ValueError, match="Input string must contain only '0' or '1' characters."):
        binary_to_decimal("102")
    with pytest.raises(ValueError, match="Input string must contain only '0' or '1' characters."):
        binary_to_decimal("abc")
    with pytest.raises(ValueError, match="Input string must contain only '0' or '1' characters."):
        binary_to_decimal("1 0 1") # Spaces are not binary
    with pytest.raises(ValueError, match="Input string must contain only '0' or '1' characters."):
        binary_to_decimal("1.0")
    with pytest.raises(ValueError, match="Input string must contain only '0' or '1' characters."):
        binary_to_decimal("-101")
    with pytest.raises(ValueError, match="Input string must contain only '0' or '1' characters."):
        binary_to_decimal("hello")

def test_binary_to_decimal_mixed_invalid_and_valid_chars():
    """
    Tests binary_to_decimal with strings containing a mix of valid and invalid characters.
    """
    with pytest.raises(ValueError, match="Input string must contain only '0' or '1' characters."):
        binary_to_decimal("101a01")
    with pytest.raises(ValueError, match="Input string must contain only '0' or '1' characters."):
        binary_to_decimal("101_01")