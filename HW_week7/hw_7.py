from operator import itemgetter


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


my_list = ["apple", "banana", "cherry", "date"]
index = 0

while index < len(my_list):
    print(my_list[index])
    index += 1


# ------------
# Custom Sorting with key Argument:
    # To sort based on a different element within the tuples (e.g., the second element,
    # or a calculated value), use the key rgument with a lambda function or itemgetter.


data = [(4, 1), (3, 2), (1, 5), (2, 8)]

# Sort by the second element using lambda
sorted_by_second = sorted(data, key=lambda x: x[1])
print(sorted_by_second)
# Output: [(4, 1), (3, 2), (1, 5), (2, 8)]

# Sort by the second element using itemgetter (often more efficient for simple indexing)
sorted_by_second_itemgetter = sorted(data, key=itemgetter(1))
print(sorted_by_second_itemgetter)
# Output: [(4, 1), (3, 2), (1, 5), (2, 8)]


# -------------
# If you have a tuple containing lists, and you want to sort each list within that tuple,
# you can use a list comprehension combined with sorted() and tuple().

a = ([2, 1, 5], [1, 5, 7], [5, 6, 5])
sorted_lists_in_tuple = tuple([sorted(i) for i in a])
print(sorted_lists_in_tuple)
# Output: ([1, 2, 5], [1, 5, 7], [5, 5, 6])

# ------------
