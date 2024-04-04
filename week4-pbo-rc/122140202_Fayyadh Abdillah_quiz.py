import random

class HangmanGame:
    def __init__(self, words, max_attempts):
        self.words = words
        self.max_attempts = max_attempts
        self.chosen_word = random.choice(self.words)
        self.display = ['_'] * len(self.chosen_word)
        self.attempts_left = max_attempts

    def guess(self, letter):
        if letter in self.chosen_word:
            for idx, char in enumerate(self.chosen_word):
                if char == letter:
                    self.display[idx] = letter
        else:
            self.attempts_left -= 1

    def is_game_over(self):
        if '_' not in self.display:
            print('Kamu Menang!')
            return True
        elif self.attempts_left == 0:
            print('Kamu kalah! Kata yang benar adalah:', self.chosen_word)
            return True
        return False

    def display_hangman(self):
        stages = [  
            """
            _____________
            |           |
            |
            |
            |
            |
            |
            |___
            """,
            """
            _____________
            |           |
            |           O
            |
            |
            |
            |
            |___
            """,
            """
            _____________
            |           |
            |           O
            |           |
            |
            |
            |
            |___
            """,
            """
            _____________
            |           |
            |           O
            |          /|\\
            |
            |
            |
            |___
            """,
            """
            _____________
            |           |
            |           O
            |          /|\\
            |          /
            |
            |
            |___
            """,
            """
            _____________
            |           |
            |           O
            |          /|\\
            |          / \\
            |
            |
            |___
            """
        ]
        return stages[self.max_attempts - self.attempts_left]

words = [
    'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
]


max_attempts = 6


hangman_game = HangmanGame(words, max_attempts)

print('QUIZ PBO')
print('Hangman Game')
while not hangman_game.is_game_over():
    print(' '.join(hangman_game.display))
    print(hangman_game.display_hangman())
    guess = input("Tebak huruf: ").lower()
    hangman_game.guess(guess)

