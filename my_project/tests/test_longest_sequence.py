import pytest
from usecases.longest_subsequence import max_seq

testdata_true = [
    ([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42],5),
    ([1, 9, 3, 10, 4, 20, 2], 4)
]

testdata_false = [
    ([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42],4),
    ([1, 9, 3, 10, 4, 20, 2], 2)
]

@pytest.mark.parametrize("input, output", testdata_true)
def test_longest_sequence_true(input, output):
    assert max_seq(input) == output


@pytest.mark.parametrize("input, output", testdata_false)
def test_longest_sequence_false(input, output):
    assert max_seq(input) != output