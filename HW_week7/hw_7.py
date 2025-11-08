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
