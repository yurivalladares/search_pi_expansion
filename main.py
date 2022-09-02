import src.settings
from src.conditions import is_palindrome, is_prime
from src.searchapi import search_pi_api

def main():

    #Hint: At condition_list, conditions with smaller time complexity should come first to benefit from short circuit evaluation

    search_pi_api(
        start_position=1,
        digits=7,
        reverse=False,
        condition_list=[
            is_palindrome,
            is_prime
        ]
    )

if __name__ == '__main__':
    main()

