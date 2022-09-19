import src.conditions
import pytest


def test_is_prime_false_negative_numbers():
    assert src.conditions.is_prime(-1) == False

def test_is_prime_false_1():
    assert src.conditions.is_prime(1) == False

def test_is_prime_false_4():
    assert src.conditions.is_prime(4) == False

def test_is_prime_false_9():
    assert src.conditions.is_prime(9) == False

def test_is_prime_false_14():
    assert src.conditions.is_prime(14) == False

def test_is_prime_false_n():
    assert src.conditions.is_prime(25) == False

def test_is_prime_true_2():
    assert src.conditions.is_prime(2) == True

def test_is_prime_true_3():
    assert src.conditions.is_prime(3) == True
    
def test_is_prime_true_n():
    assert src.conditions.is_prime(11) == True

def test_is_palindrome_true():
    assert src.conditions.is_palindrome(1331) == True

def test_is_palindrome_false():
    assert src.conditions.is_palindrome(1325) == False

def test_is_palindrome_string():
    assert src.conditions.is_palindrome('1331') == True

def test_conditions_wraper_true():
    condition_list = [src.conditions.is_prime, src.conditions.is_palindrome]
    number = 181
    assert src.conditions.condition_wraper(condition_list=condition_list, number=number) == [True, True]

def test_conditions_wraper_expection_empty_conditions():
    condition_list = []
    number = 181
    with pytest.raises(ValueError):
        src.conditions.condition_wraper(condition_list=condition_list, number=number)



