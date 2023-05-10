# a set of functions that translates user input into usable data (stuff that the program understands)
from typing import List


def difficulty() -> int:
    difficulty_level = input("\033[1;97mEnter a difficulty level (easy, medium, hard): \033[0m")
    if difficulty_level.lower() == "easy":
        return 10
    elif difficulty_level == "medium":
        return 7
    elif difficulty_level == "hard":
        return 5
    else:
        print("\033[1;97mNot a valid input, difficulty level set to hard!\033[0m")
        return 5


def get_guess(guessed_letters: List[str]) -> str:
    letter = input("\033[1;93mEnter a letter: ")
    while not letter.isalpha() or len(letter) != 1 or letter in guessed_letters:
        if letter in guessed_letters:
            print("\033[1;31mLetter guessed already\033[0m")
        else:
            print("\033[1;31mNot a valid input\033[0m")
        letter = input("\033[1;93mRe-enter a letter: \033[0m")
    return letter.lower()


def replay() -> bool:
    reply = input("\033[1;96mREPLAY? (YES or NO): \033[0m")
    while not reply.lower() == "yes" and not reply.lower() == "no":
        print("Invalid Input")
        reply = input("REPLAY? (YES or NO): ")
    if reply.lower() == "yes":
        return True
    return False
