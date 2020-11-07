#Python code that creates a password for a user following specific formatting
lengthGood = False
charGood = True
symbolGood = False
listGood = False
passwords = ["linda!@hottie","lolap@$8","chol@12"]

while True:
    pas = input('Input Password: ')
    if pas not in passwords:
        listGood = True
    else:
        pass
    if len(pas) > 8:
        lengthGood = True
    for char in pas:
        if char.isalpha() or char.isdigit() or char in "[!#$%@*]":
            pass
        else:
            charGood = False
        if char in "[!#$%@*]":
            symbolGood = True
        else:
            pass

    if lengthGood and charGood and symbolGood and listGood:
        break
    else:
        if not lengthGood:
            print("length bad")
        if not charGood:
            print("bad characters")
        if not symbolGood:
            print("not enough symbols")
        if not listGood:
            print("passwork taken")
