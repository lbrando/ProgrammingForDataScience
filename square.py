"""Create a function called `square_and_filter_even` that takes a list of numbers as input, squares each
number, and returns a new list containing only the squared values of even numbers."""

def square_and_filter_even(numbers):
    return list(filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, numbers)))

# Example usage:
numbers = [1, 2, 3, 4]
result = square_and_filter_even(numbers)
print(result) 