def print_centered_asterisk_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        asterisks = '*' * (2 * i - 1)
        print(spaces + asterisks)
print_centered_asterisk_triangle(5)
