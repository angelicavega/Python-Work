#Python code that helps user divide
def divisor2_3(x):
    if (x%2) == 0:
        if (x%3) == 0:
           print("it can be divided by both 2 and 3")
        else:
            print("it can only be divided by 2 but not 3")

    else:
        if (x%3) == 0:
            print("it can only be divided by 3 but not 2")
        else:
            print("it can not be divided by neither 2 or 3")

#text examples
divisor2_3(8)
divisor2_3(2)
divisor2_3(13)
