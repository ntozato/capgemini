from challenges.challenge3 import anagrams

def test_if_function_anagrams_returns_a_int_number():
    assert type(anagrams('ovo')) == int
    assert type(anagrams('ifailuhkqq')) == int


def test_if_function_returns_correct_pairs_of_anagrams():
    assert anagrams('ovo') == 2
    assert anagrams('ifailuhkqq') == 3
