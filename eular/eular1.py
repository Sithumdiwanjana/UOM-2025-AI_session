def sum_of_multiples(limit):
    """
    Calculate the sum of all multiples of 3 or 5 below the given limit.

    :param limit: The upper limit (exclusive) to consider for multiples.
    :return: The sum of all multiples of 3 or 5 below the limit.
    """
    total_sum = 0
    for number in range(limit):
        if number % 3 == 0 or number % 5 == 0:
            total_sum += number
    return total_sum

