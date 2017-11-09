infile = open('alice.txt','r')
import string
count = {}
for line in infile:
    for word in line.split():
        for i in list(string.punctuation):
            word = word.replace(i,' ')
        word = word.lower()
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1
keys = count.keys()

out = open('alice_words.txt', 'w')
out.write("Word \t \t \t \t Count \n")
out.write("=====================================\n")
for word in sorted(keys):
    out.write(word + "\t \t \t \t " + str(count[word]))
    out.write('\n')

print("The word 'alice' appears " + str(count['alice']) + " times in the book.")
print()

length_count = 0
longest_word = ''
for keys in count.keys():
    if len(keys) > length_count:
        length_count = len(keys)
        longest_word = keys
print("The longest word is", longest_word)
print("It has",length_count,"characters")
