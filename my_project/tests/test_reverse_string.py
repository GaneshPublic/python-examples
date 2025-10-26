import pytest
from usecases.reverse_string import reverse

testdata_true = [
    ("reverse", "esrever"),
    ("help", "pleh"),
]

testdata_false = [
    ("reverse", "reverse"),
    ("help", "help"),
]

@pytest.mark.parametrize("input, output", testdata_true)
def test_reverse_string_true(input, output):
    assert reverse(input) == output

@pytest.mark.parametrize("input, output", testdata_false)
def test_reverse_string_false(input, output):
    assert reverse(input) != output