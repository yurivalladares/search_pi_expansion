def condition_wraper(condition_list: list, number: int) -> list:
    if not condition_list:
        raise ValueError('condition_list cannot be empty')
    return [condition(number) for condition in condition_list]


def is_prime(x: int) -> bool:
    if x<=1:return False
    if x==2 or x==3:return True
    if x%2==0 or x%3==0:return False
    for i in range(5, int(x**0.5)+1, 6):
        if x%i==0 or x%(i+2)==0:return False
    return True


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]