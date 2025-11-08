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
