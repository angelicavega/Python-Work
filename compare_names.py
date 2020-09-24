def comparenames(inputname, yourname, othername1, othername2, othername3):
    if (inputname == yourname):
        print('this is a nice name')
    elif (inputname == othername1):
        print('you are famous!')
    elif (inputname == othername2):
        print('this is a bad name')
    else:
        print('I wish I could meet you!')

inputname = input('What is your name?')

yourname = 'Angelica'

othername1 = 'Peter Pan'

othername2 = 'Trump'

othername3 = 'Marie Curie'

comparenames(inputname, yourname, othername1, othername2, othername3)
    
