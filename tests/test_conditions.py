import src.conditions
import pytest


def test_not_prime():
    assert src.conditions.is_prime(-1) == False
    assert src.conditions.is_prime(1) == False
    assert src.conditions.is_prime(4) == False
    assert src.conditions.is_prime(9) == False
    assert src.conditions.is_prime(14) == False
    assert src.conditions.is_prime(25) == False

def test_is_prime():
    assert src.conditions.is_prime(2) == True
    assert src.conditions.is_prime(3) == True
    assert src.conditions.is_prime(11) == True

def test_not_palindrome():
    assert src.conditions.is_palindrome(1325) == False
    assert src.conditions.is_palindrome('1325') == False

def test_is_palindrome():
    assert src.conditions.is_palindrome(1331) == True
    assert src.conditions.is_palindrome('1331') == True

def test_conditions_wraper_true():
    condition_list = [src.conditions.is_prime, src.conditions.is_palindrome]
    number = 181
    assert src.conditions.condition_wraper(condition_list=condition_list, number=number) == [True, True]

def test_raise_exception_empty_conditions():
    condition_list = []
    number = 181
    with pytest.raises(ValueError):
        src.conditions.condition_wraper(condition_list=condition_list, number=number)



