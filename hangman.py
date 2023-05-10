# the game itself

import random
from wordwrapper import WordWrapper


class Hangman:
    WORD_BANK = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes",
                 "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm",
                 "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords",
                 "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl",
                 "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus",
                 "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove",
                 "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour",
                 "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard",
                 "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker",
                 "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking",
                 "jovial", "joyful", "juicy", "juicebox", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki",
                 "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky",
                 "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha",
                 "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama",
                 "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling",
                 "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm",
                 "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength",
                 "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew",
                 "topaz", "transcript", "transgress", "transplant", "twelfth", "unknown", "unworthy", "unzip", "uptown",
                 "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy",
                 "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard",
                 "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy",
                 "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]

    def __init__(self, tries_remaining: int):
        self.is_complete = False
        self.tries_remaining = tries_remaining
        self.word_wrapper = WordWrapper(self.WORD_BANK[random.randrange(len(self.WORD_BANK))])
        self.guessed_letters = []

    def check_guess(self, guess: str) -> None:
        if not self.word_wrapper.check_guess(guess):
            self.tries_remaining -= 1
        self.guessed_letters.append(guess)
        if self.word_wrapper.all_true() or self.tries_remaining == 0:
            self.is_complete = True

    def is_win(self) -> bool:
        return self.tries_remaining > 0 and self.is_complete





