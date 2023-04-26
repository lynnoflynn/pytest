import pytest

from script.add import add


# def setup_module():
#     print("Test begins.")


def teardown_module():
    print("Test ends.")


def setup_function():
    print("Calculation begins.")


def teardown_function():
    print("Calculation ends.")


@pytest.mark.parametrize(
    "a, b,  expected",
    [
        [1, 0, 1],
        [-0.01, 0.02, 0.01],
        [-0.01, 0, -0.01],
        [99.01, 0, "a is invalid input due to data value."],
        [1, -99.01, "b is invalid input due to data value."],
        ["文", 9.3, "a is invalid input due to data format."],
        [10.01, "", "b is invalid input due to data format."]

    ],
    ids =
    ["a and b are integers",
     "a and b are floats",
     "a is integer and b is float",
     "a is not in the range",
     "b is not in the range",
     "The data type of a is not valid",
     "The data type of b is not valid"
     ]
)

def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected

