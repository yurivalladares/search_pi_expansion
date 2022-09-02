import src.settings
from src.conditions import is_palindrome, is_prime
from src.searchapi import search_pi_api
from src.searchfile import *

def main():
    # conditions with smaller time complexity should come first to benefit from short circuit evaluation
    search_pi_api(
        start=1,
        digits=7,
        condition_list=[
            is_palindrome,
            is_prime
        ])

if __name__ == '__main__':
    main()