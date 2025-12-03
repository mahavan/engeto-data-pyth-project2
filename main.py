"""
Project 2: Game Bulls & Cows
"""
import random

def print_introduction() -> str:
    print("""
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
""")
    
def create_secret_number() -> str:
    """
    Generate a number with unique digits as a string of NUMBER_LENGTH 
    digits, where the first digit is not zero.
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

   

