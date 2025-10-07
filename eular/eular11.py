def largest_product_in_a_grid(grid, n):
    """Find the largest product of n adjacent numbers in the same direction (up, down, left, right, or diagonally) in the given grid."""
    max_product = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            # Right
            if c + n <= cols:
                product = 1
                for i in range(n):
                    product *= grid[r][c + i]
                max_product = max(max_product, product)

            # Down
            if r + n <= rows:
                product = 1
                for i in range(n):
                    product *= grid[r + i][c]
                max_product = max(max_product, product)

            # Diagonal right-down
            if r + n <= rows and c + n <= cols:
                product = 1
                for i in range(n):
                    product *= grid[r + i][c + i]
                max_product = max(max_product, product)

            # Diagonal left-down
            if r + n <= rows and c - n >= -1:
                product = 1
                for i in range(n):
                    product *= grid[r + i][c - i]
                max_product = max(max_product, product)

    return max_product