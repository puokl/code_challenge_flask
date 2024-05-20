def is_power_of_two(num):
    if num < 1:
        return False
    return (num & (num - 1)) == 0
