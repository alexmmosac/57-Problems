import pytest
import sys 
sys.path.insert(0, "src/")
import Saying_hello_Ex_1

def test_Brian(monkeypatch: pytest.MonkeyPatch):
	inputs = "Brian"
	monkeypatch.setattr("builtins.input", lambda x: inputs)
	results = Saying_hello_Ex_1.main()
	assert results == "Hello, Brian, Nice to meet you!"

def test_Alex(monkeypatch: pytest.MonkeyPatch):
	inputs = "Alex"
	monkeypatch.setattr("builtins.input", lambda x: inputs)
	results = Saying_hello_Ex_1.main()
	assert results == "Hello, Alex, Nice to meet you!"
