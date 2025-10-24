def christmas_tree(height):
    """Generate a Christmas tree pattern of given height."""
    tree = []
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        tree.append(spaces + stars)
    trunk = ' ' * (height - 1) + '|'
    tree.append(trunk)
    return '\n'.join(tree)

christmas_tree_height = 5
print(christmas_tree(christmas_tree_height))
