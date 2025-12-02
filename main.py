"""
Project 2: Game Bulls & Cows
"""
import random

def secret_number() -> str:
    """
    Generate a unique number as a string of NUMBER_LENGTH digits, 
    where the first digit is not zero.
    """
    # Length of the secret number must be <= 10
    NUMBER_LENGTH: int = 4 
    digits: list[int] = [i for i in range(10)]
    random.shuffle(digits)
    while digits[0] == 0:
        random.shuffle(digits) 
    # Select the first NUMBER_LENGTH digits and join them into one number.
    return ''.join(map(str, digits[:NUMBER_LENGTH])) 

if __name__ == "__main__":

    print("Secret number for debugging:", secret_number())