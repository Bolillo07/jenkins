import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0
    assert calculator.add(2.5, 1.5) == 4.0

def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(-1, 1) == -2
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(2.5, 1.5) == 1.0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(0, 0) == 0
    assert calculator.multiply(2.5, 2) == 5.0

def test_divide():
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-1, 1) == -1
    assert calculator.divide(0, 5) == 0
    assert calculator.divide(2.5, 0.5) == 5.0

def test_divide_by_zero():
    assert calculator.divide(5, 0) == "Error: division by zero"
