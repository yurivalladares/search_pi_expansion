def condition_wraper(condition_list: list, number: int) -> list:
    return [condition(number) for condition in condition_list]

def is_prime(x: int) -> bool:
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5 + 1), 2):
        if x % i == 0:
            return False
    return True

def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]