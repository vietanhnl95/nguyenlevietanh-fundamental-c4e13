

while True:
    u = input("user: ")
    if u.lower() == ("c4e"):
        p = str(input("password: "))
        if p == "codethechange":
            print ("successful login")
        else:
            print ("incorrect password")
    else:
        print ("user not found")
