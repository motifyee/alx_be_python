
def safe_divide(numerator, denominator):
    try:
        n = float(numerator)
        d = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    if d == 0:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {n/d}"
