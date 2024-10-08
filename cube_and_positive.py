"""Create a function called `cube_and_filter_positive` that takes a list of numbers as input,
calculates the cube of each number, and returns a new list containing only the positive cube values (greater than 0)."""

def cube_and_filter_positive(numbers):
    return list(filter(lambda x: x > 0, map(lambda x: x ** 3, numbers)))

# Example usage:
numbers = [-3, -2, -1, 0, 1, 2, 3]
result = cube_and_filter_positive(numbers)
print(result) 