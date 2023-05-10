from typing import List

from wordwrapper import WordWrapper

from colorama import init
init()

# from [file] import [class]
# consists of functions that presents to the users


def word_covered(word_wrapper: WordWrapper) -> None:
    result = ""
    for guess in word_wrapper.guesses:
        if guess:
            result += word_wrapper.word[len(result)]
        else:
            result += "_"
    print("\033[1;39m" + result + "\033[0m")


def tries_remaining(tries_remaining: int) -> None:
    print("\033[1;91mTries remaining: " + str(tries_remaining) + "\033[0m")


def print_result(is_win: bool) -> None:
    if is_win:
        print("\033[1;92mYOU HAVE WON THE GAME! ^_^ $_$ *_* @_@\033[0m") # change colour of text
    else:
        print("\033[1;31mYOU DIED X_X\033[0m") # add audio


def print_word(word: str) -> None:
    print("\033[1;35mTHE WORD WAS: " + word.upper())


def print_guessed_letters(guess: str) -> None:
    print("\033[1;90mLetters guessed: " + str(guess))


def print_end_game() -> None:
    print("\033[1;94mGame Over, Thanks for Playing :)")