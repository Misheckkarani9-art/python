# Python functions
# They are a block of code / statement that performs a given task /action.They can be reused througgh ouut the program to perform different tasks
# Functions are deefined using the def keyword. (define)
# We have two main types of functions
# 1.  In-built functions ->They come preinstalled with the interpreter i.e print() ,pop() etc
# 2.  User defined functions ->They are created by the programmer to solve  a given task.
# To define a function you need to give it a name followeed by ()



def greetings():
    print("hello there")
# below we call the function by the use of its name
greetings()


print('==================================')

# Additional function
def addition ():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)
addition()

print('==================================')

def multiply():
    num1 = 20
    num2 = 30
    num3 = 10
    product =num1 * num2 * num3
    print("the product is: ",product)
multiply()

print('==================================')

# Below is adivision function
def divide():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    quotient =num1 / num2
    print("The answer is: ",quotient)
    print("--------")
for function in range (3):
    divide()
