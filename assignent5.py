# no1

def calculate_rectangle_area():
    length = 5  # You can set any value here
    width = 3   # You can set any value here
    area = length * width
    print(f"The area of the rectangle is {area}.")

# Call the function
calculate_rectangle_area()

print('===================')

# no2
def calculate_operations(num1, num2):
    sum_result = num1 + num2
    diff_result = num1 - num2
    prod_result = num1 * num2
    # To avoid division by zero, we can add a check
    if num2 != 0:
        div_result = num1 / num2
    else:
        div_result = "Undefined (division by zero)"

    return sum_result, diff_result, prod_result, div_result

# Example usage
result = calculate_operations(10, 2)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Division:", result[3])

# no3
print('===================')

def check_number():
    try:
        num = float(input("Enter a number: "))
        if num > 0:
            print("The number is positive.")
        elif num < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function
check_number()

print('===================')

# no4
def sum_of_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

# Example usage
n = 5
result = sum_of_numbers(n)
print(f"The sum of numbers from 1 to {n} is {result}.")

print('===================')


#  no5
def print_squares_upto_n():
    try:
        n = int(input("Enter a number: "))
        i = 1
        while i <= n:
            square = i ** 2
            print(f"The square of {i} is {square}.")
            i += 1
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Call the function
print_squares_upto_n()



