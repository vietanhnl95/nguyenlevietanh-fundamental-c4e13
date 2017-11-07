teen_dict = {
    'ngta': "nguoi ta",
    'gato': "ghen an tuc o",
    'r': "roi",
    'ik': "di",
    'hc': "hoc",
}
while True:
    n1 = str(input("Choose a word: "))
    if n1 in teen_dict:
        print("Your word: ",n1)
        print("Translation:", teen_dict[n1])
    else:
        n2 = str(input("This word is not in my knowledge. Do u want to tell me?(Y/N) "))
        if n2.upper() == 'N':
            print("OK. See Ya.")
        if n2.upper() == 'Y':
            n3 = str(input("Tell me its meaning: "))
            teen_dict[n1] = n3
            print("Updated")
            print(teen_dict)
    n4 = input("Continue to look up? (Y/N) ")
    if n4.upper() == 'Y':
        print('Ok')
    else:
        print('See Ya')
        break
