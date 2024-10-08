"""Create a function called `double_and_filter_odd` that takes a list of numbers as input, doubles each
number, and returns a new list containing only the doubled values of odd numbers."""

def double_and_filter_odd(numbers):
    return list(map(lambda x: x * 2, filter(lambda x: x % 2 != 0, numbers)))

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
result = double_and_filter_odd(numbers)
print(result)