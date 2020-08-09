from_user = map(int, input("Enter space separated numbers: ").split())
def median(from_user):
    set_from_user = list(from_user)

    if not set_from_user:
            print(input("Median not defined"))
    if not all([isinstance(v, (int,float)) for v in set_from_user]):
            print(input("'Values' must be a list of int or float"))


    center   = len(set_from_user)/2


    if len(set_from_user) % 2:
        return float(set_from_user[center])
    else:
        return (set_from_user[center-1]+set_from_user[center])/2.0
#set_from_user.sort()

print(median(from_user))
