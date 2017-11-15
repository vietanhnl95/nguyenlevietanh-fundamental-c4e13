word_list = ["january","february","march","april","may","june","july","august","september","october","november","december"]
picture = [
"""
 |-------
 |      O
 |    --|--
 |     / \\
 |
_|_
""",
"""
 |-------
 |      O
 |    --|--
 |     /
 |
_|_
""",
"""
 |-------
 |      O
 |    --|--
 |
 |
_|_
""",
"""
 |-------
 |      O
 |    --|
 |
 |
_|_
""",
"""
 |-------
 |      O
 |      |
 |
 |
_|_
""",
"""
 |-------
 |      O
 |
 |
 |
_|_
"""
]
from random import choice
import string
alphabet = list(string.ascii_lowercase)
guessed = []

print("I want to play a game. Guess which month is this?")
word = choice(word_list)

character = list(word)

count = 0

base = list("_" * len(character))
print(*base)

while count < 5:
    guess = input("Guess a letter: ")
    if guess not in alphabet:
        print("It's not a letter")
    elif guess in guessed:
        print("U have already guessed this letter. Choose another letter.")
    else:
        guessed.append(guess)
        if guess not in character:
            count += 1
            print(picture[5-count])
        else:
            for i in range(len(character)):
                if character[i] == guess:
                    base[i] = guess
            print(picture[5-count])        
        print(*base)
        if "_" not in base:
            print("U WIN")
            break
else:
    print("U LOSE")
