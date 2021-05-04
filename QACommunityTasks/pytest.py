import pytest

def func(num):
    return num * 2

def test_answer():
    assert func(6) == 10
def test_answer1():
    assert func(7) == 10

test_answer()
test_answer1()
