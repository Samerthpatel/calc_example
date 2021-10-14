"""content of calculator.py"""
def inc(x_value):
    """increment function adds one to the x_value"""
    return x_value + 1
def test_answer():
    """this tests the function"""
    assert inc(4) == 5
