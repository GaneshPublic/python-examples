# This we can add if we don't want to use setup.py
#import sys
#import os

# Add the project directory to sys.path
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from usecases.anagram import anagram    

def test_anagram_true():
    assert anagram("Tar", "Rat") == True

def test_anagram_false():
    assert anagram("Arc", "Orc") == False