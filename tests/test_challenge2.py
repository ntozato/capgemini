from challenges.challenge2 import verify_password


def test_if_function_password_returns_int_number():
    assert type(verify_password('Ya3')) == int
    assert type(verify_password('aA1*ab')) == int


def test_if_function_returns_correct_value():
    assert verify_password('Ya3') == 3
    assert verify_password('Ya3a') == 2
    assert verify_password('a') == 5
    assert verify_password('ab') == 4
    assert verify_password('abc') == 3
    assert verify_password('abcd') == 3
    assert verify_password('abcde') == 3
    assert verify_password('abcdef') == 3
    assert verify_password('abcdefg') == 3
    assert verify_password('Abcdefg') == 2
    assert verify_password('A*cdefg') == 1
    assert verify_password('aA1*') == 2
    assert verify_password('aA1*a') == 1
    assert verify_password('aA1*ab') == 0
