"""
Project 2: Game Bulls & Cows
"""
import random
import textwrap

def print_introduction() -> None:
    print(textwrap.dedent("""
        Hi there!
        -----------------------------------------------
        I've generated a random 4 digit number for you.
        Let's play a bulls and cows game.
        -----------------------------------------------
    """))
    
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

def validate_input(number: str) -> str:
    """
    Validate the user's input and return an error message if invalid.
    """
    if not number.isdigit():
        return (
            "The entered number must contain digits only. "
            "Please try again!"
        )
    if len(number) != 4:
        return (
            "The entered number must be 4 digits long. "
            "Please try again!"
        )
    if len(set(number)) != 4:
        return (
            "The entered number must not contain the same digits. "
            "Please try again!"
        )
    if number[0] == '0':
        return (
            "The entered number must not start with a zero. "
            "Please try again!"
        )
    return ""

def print_results(bulls: int, cows: int, attempts: int) -> None:
    if bulls == 4:
        print("Correct, you've guessed the right number "
            f"in {attempts} guesses!")
        print("-----------------------------------------------")
        print("That's amazing!")
        exit()
    else:
        bulls_word = "bull" if bulls == 1 else "bulls"
        cows_word = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bulls_word}, {cows} {cows_word}")
        print("-----------------------------------------------")
    

if __name__ == "__main__":

    print_introduction()
    secret_number: str = create_secret_number()
    attempts = 0

    while True:
        print(f"Secret number for debugging: {secret_number}")
        number: str = input("Enter a number: ")
        error_message = validate_input(number)
        if error_message:
            print(error_message)
            continue

        attempts += 1

        bulls: int = sum(
            1 
            for secret_digit, guess_digit in zip(secret_number, number) 
            if secret_digit == guess_digit
        )
        cows: int = sum(
            1 
            for guess_digit in number 
            if guess_digit in secret_number
        ) - bulls

        print_results(bulls, cows, attempts)

