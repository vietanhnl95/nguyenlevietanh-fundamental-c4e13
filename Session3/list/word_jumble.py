from random import choice

word = "funny"
char_list = []
characters = list(word)
while characters != []:
    c = choice(characters)
    characters.remove(c)
    char_list.append(c)
print(*char_list, sep = ' ')
while True:
    guess = input("Guess the word: ")
    if guess == word:
        print("congrats!!")
        break
    else:
        print("nope :D")
