# loops
# ->some times we may need to do a piece of work a number of repeated times and in such we may use loops.
# A loop is a control structures that allows us to execute a block of code repeatedly until a certain conditioon is net.
# examples -> for loop  and while loop

#Below is a syntax for loop in python

"""
for valuuable in range (n):
   # block of code to be executed

"""

# print("hello there")
# print("hello there")
# print("hello there")
# print("hello there")
# print("hello there")

for greeting in range (5):
    print("helo there", greeting)


print('=======================')


for number in range (10 ,20):
    print(number)


print('=======================')

for number in range( 50 ,71 ,2):
    print(number)


print('=======================')
# odd numbers
for number in range (101 , 150 ,2):
    print(number) 

print('=======================')

for number in range (201 , 149,1):
    if number % 3 ==0:
        print(number)

print('=======================')
for number in range (2000 ,2024):
    print()