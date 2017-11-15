alice_file = open('alice.txt')
text = alice_file.read()
alice_file.close()

import string
ignore_words = list(string.punctuation)
ignore_words.append('\n')

for i in ignore_words:
    text = text.replace(i,'')
words = text.split(' ')

word_count = {}
for word in words:
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
