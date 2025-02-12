from csv import excel

import pytest
import calculator

def test_calculator_power_1():
    #arrange
    a:int = 4
    b:int = 2
    expected: int = 16

    #act
    actual: int = calculator.power(a,b)

    #assert
    assert expected == actual, "powering the given first number by the second"

def test_calculator_power_2():
    #arrange
    a:int = 3
    b:int = 2
    expected: int = 9

    #act
    actual: int = calculator.power(a,b)

    #assert
    assert expected == actual, "powering the given first number by the second"

def test_calculator_sqrt_1():
    #arrange
    a:int = 25
    expected: int = 5

    #act
    actual: int = calculator.sqrt(a)

    #assert
    assert expected == actual, "Square root the given number"

def test_calculator_sqrt_2():
    #arrange
    a:int = -5

    #act
    with pytest.raises(ValueError):
        calculator.sqrt(a)

def test_calculator_factorial_1():
    #arrange
    a: int = 4
    expected: int = 24

    #act
    actual: int = calculator.factorial(a)

    #assert
    assert expected == actual, "factorising the given number"

def test_calculator_factorial_2():
    # arrange
    a: int = 5
    expected: int = 120

    # act
    actual: int = calculator.factorial(a)

    # assert
    assert expected == actual, "factorising the given number"

def test_calculator_factorial_3():
    # arrange
    a: int = -3
    # act
    with pytest.raises(ValueError):
        calculator.factorial(a)