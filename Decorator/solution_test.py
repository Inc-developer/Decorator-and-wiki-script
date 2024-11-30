from solution import *


def test_numbers_ok():
    assert sum_two(1, 2) == 3.0
    assert sum_two(564554, 7657657) == 8222211


def test_numbers_error():
    assert sum_two(1, 8.6) == TypeError
    assert sum_two(654.4, 8) == TypeError


def test_str_ok():
    assert hello_name("John") == "Hello John"


def test_str_error():
    assert hello_name(5) == TypeError
