def Special_Pythagorean_triplet(n):
    """Find the product of the Pythagorean triplet for which a + b + c = n."""
    for a in range(1, n):
        for b in range(a, n - a):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None