from anagram import is_anagram

def test_simple_anagram():
    assert is_anagram("listen", "silent") is True

def test_not_anagram():
    assert is_anagram("hello","world") is False 

def test_case_insensitive():
    assert is_anagram("Listen", "Silent") is True 

def test_with_spaces():
    assert is_anagram("rail safety", "fairy tales") is True

def test_different_lengths():
    assert is_anagram("cat", "cats") is False