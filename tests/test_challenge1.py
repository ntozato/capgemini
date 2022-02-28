from challenges.challenge1 import asterisk_triangle

def test_if_asterisk_triangle_returns_a_string():
    assert type(asterisk_triangle(6)) == str

def test_if_function_asterisk_triangle_returns_correct_value():
    assert asterisk_triangle(6) == "     *\n    **\n   ***\n  ****\n *****\n******"
    assert asterisk_triangle(3) == "  *\n **\n***"
    assert asterisk_triangle(1) == "*"
    assert asterisk_triangle(0) == ""