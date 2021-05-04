import double
import pytest

def test_answer():
    assert double.func(6) == 10

def test_answer1():
    assert double.func(7) == 10

test_answer()
test_answer1()