def sum_square_difference(n):
    """Find the difference between the sum of the squares of the first n natural numbers and the square of the sum."""
    sum_of_squares = sum(i**2 for i in range(1, n + 1))
    square_of_sum = sum(range(1, n + 1))**2
    return square_of_sum - sum_of_squares