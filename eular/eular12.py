def highly_divisible_triangular_number(n):
    """Find the first triangular number with over n divisors."""
    def count_divisors(x):
        count = 0
        for i in range(1, int(x**0.5) + 1):
            if x % i == 0:
                count += 2 if i != x // i else 1
        return count

    triangle = 0
    i = 1
    while True:
        triangle += i
        if count_divisors(triangle) > n:
            return triangle
        i += 1