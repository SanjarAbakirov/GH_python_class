def find_largest_number(numbers):
    """
    This algorithm finds the largest number in a given list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        int or float: The largest number in the list.
                      Returns None if the list is empty.
    """
    if not numbers:
        return None  # Handle empty list case

    max_num = numbers[0]  # Initialize max_num with the first element

    for num in numbers:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found

    return max_num


# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
largest = find_largest_number(my_list)
print(f"The largest number in the list is: {largest}")

empty_list = []
largest_empty = find_largest_number(empty_list)
print(f"The largest number in the empty list is: {largest_empty}")

# -----------


def check_positive_and_even(number):
    """
    Checks if a number is both positive and even using boolean logic.

    Args:
      number: An integer to be evaluated.

    Returns:
      True if the number is positive and even, False otherwise.
    """
    is_positive = number > 0
    is_even = number % 2 == 0

    # Combine the boolean conditions using the 'and' operator
    is_positive_and_even = is_positive and is_even

    return is_positive_and_even


# Example usage:
num1 = 10
result1 = check_positive_and_even(num1)
# Output: Is 10 positive and even? True
print(f"Is {num1} positive and even? {result1}")

num2 = -4
result2 = check_positive_and_even(num2)
# Output: Is -4 positive and even? False
print(f"Is {num2} positive and even? {result2}")

num3 = 7
result3 = check_positive_and_even(num3)
# Output: Is 7 positive and even? False
print(f"Is {num3} positive and even? {result3}")

num4 = 0
result4 = check_positive_and_even(num4)
# Output: Is 0 positive and even? False
print(f"Is {num4} positive and even? {result4}")
