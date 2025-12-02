from app.split_integer import split_integer

import pytest


@pytest.mark.parametrize(
    "value, nop, exp", [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
class Tests:
    def test_sum_of_the_parts_should_be_equal_to_value(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        actual = split_integer(value, nop)
        assert sum(actual) == value

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        actual = split_integer(value, nop)
        assert len(actual) == nop

    def test_should_return_part_equals_to_value_when_split_into_one_part(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        actual = split_integer(value, nop)
        if len(actual) > 0:
            assert max(actual) - min(actual) <= 1

    def test_parts_should_be_sorted_when_they_are_not_equal(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        actual = split_integer(value, nop)
        assert actual == sorted(actual)

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
            self,
            value: int,
            nop: int,
            exp: list) -> None:
        actual = split_integer(value, nop)
        assert actual == exp
