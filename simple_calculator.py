# This function adds two numbers 
def add(num1, num2):
   return num1 + num2

# This function subtracts two numbers 
def subtract(num1, num2):
   return num1 - num2

# This function multiplies two numbers
def multiply(num1, num2):
   return num1 * num2

# This function divides two numbers
def divide(num1, num2):
   return num1 / num2

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Here we take the input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
