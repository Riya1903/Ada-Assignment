def multiply(x, y):
    # Base case: If either x or y is a single-digit number, return their product
    if x < 10 or y < 10:
        return x * y

    # Calculate the number of digits in x and y
    num_digits = max(len(str(x)), len(str(y)))
    mid = num_digits // 2

    # Split x and y into halves
    high1, low1 = divmod(x, 10 ** mid)
    high2, low2 = divmod(y, 10 ** mid)

    # Recursive calls to multiply the halves
    z0 = multiply(low1, low2)
    z1 = multiply((low1 + high1), (low2 + high2))
    z2 = multiply(high1, high2)

    # Compute the final result using the subproblems' solutions
    return (z2 * 10 ** (2 * mid)) + ((z1 - z2 - z0) * 10 ** mid) + z0


# Example usage:
x = 12345678901234567890
y = 98765432109876543210
result = multiply(x, y)
print(result)
