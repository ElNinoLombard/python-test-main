import tests

def test_add():
    assert tests.add(3, 5) == 8

def test_subtract():
    assert tests.subtract(10, 4) == 6

def test_multiply():
    assert tests.multiply(2, 6) == 12

def test_divide():
    assert tests.divide(10, 2) == 5

def test_divide_by_zero():
    try:
        tests.divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

# def test_add():
#     assert tests.add(3, 5) == 9  # Intentional failure
