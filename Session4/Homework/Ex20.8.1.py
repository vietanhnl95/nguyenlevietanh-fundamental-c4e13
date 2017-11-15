sentence = str(input("Write a sentence: "))
import string
alphabet = list(string.ascii_lowercase)
char_list = list(sentence)
# print(sentence)
# print(alphabet)
# print(char_list)

for i in alphabet:
    letter_count = 0
    for j in range(len(char_list)):
        if char_list[j].lower() == i:
            letter_count += 1
    if letter_count > 0:
        print(i, letter_count)
