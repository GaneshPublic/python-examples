import pytest
from usecases.quicksort import sort


testdata_true = [
    ([10,3,11,13,2,5,20,8,45], [2,3,5,8,10,11,13,20,40])
]

testdata_false = [
    ([10,3,11,13,2,5,20,8,45], [2,3,5,8,11,10,13,20,40])
]

@pytest.mark.parametrize("input, output", testdata_true)
def test_quicksort_true(input, output):
    assert sort(input) == output


@pytest.mark.parametrize("input, output", testdata_false)
def test_quicksort_true(input, output):
    assert sort(input) != output
