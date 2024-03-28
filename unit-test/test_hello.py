# Import the hello function from the hello module
from hello import hello #hello.py file

# Test with a default argument
def test_default():
    assert hello() == "hello, world"

# Test with an argument
def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
