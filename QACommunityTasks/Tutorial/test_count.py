import pytest
import count
import vowels
import list_of_sqaures
import factorial




def test_count_zeros():
    assert count.count([0,0,0], 0) == 3

def test_count_string():
    assert count.count(["a","a","a"], "a") == 3

def test_vowels():
    assert vowels.vowels("pony") == 1

def test_los():
    assert list_of_sqaures.list_of_squares(3) == {1:1, 2:4, 3:9}

def test_fact():
    assert factorial.fact(3) == 6

test_count_string()
test_count_zeros()
test_fact()
test_los()
test_vowels()