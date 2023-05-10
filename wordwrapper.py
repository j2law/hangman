# contains the word and other properties of the word along with methods related to the word processing

class WordWrapper:
    def __init__(self, word: str):
        self.word = word
        self.guesses = [False] * len(self.word)

    def check_guess(self, guess: str) -> bool:
        if not guess in self.word:
            return False
        for index in range(len(self.word)):
            if guess == self.word[index]:
                self.guesses[index] = True
        return True

    def all_true(self) -> bool:
        return self.guesses == [True] * len(self.word)


