#Python code that incorporates simple math operations for users
import math
def top():
    print ('******************')

def side(x):
    for y in range(0,x):
        print("*                 *")

value = input('How Tall?')
top()
side(int(value))
top()



#add two numbers
def add(x,y):
    return x+y
#subtract two numbers

def subtract(x,y):
    return x-y
#multiply
def multiply(x,y):
    return x*y
#divide
def divide(x,y):
    return x/y

#Python code that finds cost, profit, and revenue

def profit(price):
    return revenue(price)- cost(price)

def revenue(price):
    return price*attendees(price)

def cost(price):
    return attendees(price)*0.04 +180

def attendees(price):
    return 120+ (5-price) *(15/0.1)

value = input('Enter Price:')
print(profit(int(value)))



