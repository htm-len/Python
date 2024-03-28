# Unit test to test calTest.py using Pytest
import pytest

from calcTest import square

# Test positive numbers
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

# Test negative numbers
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

# Test zero
def test_zero():
    assert square(0) == 0

# Test Str 
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")