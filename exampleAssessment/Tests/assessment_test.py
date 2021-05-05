import pytest
import sys
import os
sys.path.append(os.path.abspath("/Users/vikhi/OneDrive/Documents/PythonQA/exampleAssessment"))
from Code import example

def test_endsPy():
    assert example.endsPy("ilovepy") == True
    assert example.endsPy("welovepy") == True
    assert example.endsPy("welovepyforreal") == False
    assert example.endsPy("pyiscool") == False
    assert example.endsPy("hurrayforpY") == True