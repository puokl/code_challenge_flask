def build_pyramid(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Invalid input: Number of floors must be a positive integer')
    pyramid = []
    for i in range(1, n + 1):
        pyramid.append(' ' * (n - i) + '*' * (2 * i - 1) + ' ' * (n - i))
    return pyramid
