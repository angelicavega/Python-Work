#Python Code that estimates price for users

def weeks(initialprice, numberofweeks):
    if numberofweeks=='2':
        return initialprice
    elif (numberofweeks=='3'):
        return initialprice*0.75
    elif (numberofweeks=='4'):
        return initialprice*0.50
    elif (numberofweeks=='5'):
        return initialprice*0.25
    else:
        return initialprice*.25



initialprice = input('Enter Price:')
numberofweeks = input('Enter Number of Weeks between 2-5:')
print(weeks(int(initialprice), int(numberofweeks)))


