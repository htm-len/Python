# Import the hello function from the hello module
from hello import hello #hello.py file

# Test with a default argument
def test_default():
    assert hello() == "hello, world"

# Test with an argument
def test_argument():
    assert hello("Len") == "hello, Len"