def largest_product_in_series(series, n):
    """Find the largest product of n consecutive digits in the given series."""
    max_product = 0
    for i in range(len(series) - n + 1):
        product = 1
        for j in range(n):
            product *= int(series[i + j])
        if product > max_product:
            max_product = product
    return max_product