def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

# Get user input for a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in user_input.split()]

# Calculate the sum of positive numbers
result = sum_positive_numbers(numbers_list)
print("Sum of positive numbers:", result)