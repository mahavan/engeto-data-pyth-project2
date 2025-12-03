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

def print_results(bulls: int, cows: int) -> None:
    pass

if __name__ == "__main__":

    print_introduction()
    secret_number: str = create_secret_number()
    i = 1
    while True:
        print(f"Secret number for debugging: {secret_number}")
        number: str = input("Enter a number: ")

        if not number.isdigit():
            print("The entered number must contain digits only. "
                "Please try again!")
            continue
        if len(number) != 4:
            print("The entered number must be 4 digits long. "
                "Please try again!")
            continue
        if len(set(number)) != 4:
            print("The entered number must not contain the same digits. "
                "Please try again!")
            continue
        if number[0] == '0':
            print("The entered number must not start with a zero. "
                "Please try again!")
            continue

        bulls: int = sum(1 for s, g in zip(secret_number, number) if s == g)
        cows: int = sum(1 for g in number if g in secret_number) - bulls

        print_results(bulls, cows)

        if bulls == 4:
            print(f"Congratulations! You guessed the number {secret_number} in {i} attempts.")
            break
        i += 1

