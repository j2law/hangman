import presenter
import controller
from hangman import Hangman

# to connect everything

# todo:
# get word list dynamically
# upload to github
# create executable file in python


def play():
    hangman = Hangman(controller.difficulty())
    while not hangman.is_complete:
        presenter.tries_remaining(hangman.tries_remaining)
        presenter.word_covered(hangman.word_wrapper)
        hangman.check_guess(controller.get_guess(hangman.guessed_letters))
        presenter.print_guessed_letters(hangman.guessed_letters)
    presenter.print_result(hangman.is_win())
    presenter.print_word(hangman.word_wrapper.word)


if __name__ == '__main__':
    play()
    while controller.replay():
        play()
    presenter.print_end_game()



