def summation_of_primes(n):
    """Calculate the sum of all prime numbers below n."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(i for i in range(2, n) if is_prime(i))