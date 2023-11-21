import pytest
import sys 
sys.path.insert(0, "src/")
import Counting_the_numbers_of_characters_Ex_2

def test_5_homer():
	results = Counting_the_numbers_of_characters_Ex_2.string_count("Homer")
	assert results == 5

def test_6_tester():
	results = Counting_the_numbers_of_characters_Ex_2.string_count("Tester")
	assert results == 6

def test_non_string():
	results = Counting_the_numbers_of_characters_Ex_2.string_count(6)
	assert results == None

