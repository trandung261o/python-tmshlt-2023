def calculate_power(base_number, exponent):
    result = 1
    for index in range(exponent):
        result *= base_number
    return result

print(calculate_power(10, 2))