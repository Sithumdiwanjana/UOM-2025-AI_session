def sum_even_fibonacci(limit):
    """
    Calculate the sum of all even Fibonacci numbers below the given limit.

    :param limit: The upper limit (exclusive) to consider for Fibonacci numbers.
    :return: The sum of all even Fibonacci numbers below the limit.
    """
    a, b = 0, 1
    total_sum = 0
    while b < limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b
    return total_sum


