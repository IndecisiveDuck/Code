def divide(numerator: int, denominator: int)->float:
    """Divides two numbers

    Args:
        numerator (int)
        denominator (int): must be non-zero

    Returns:
        float: _description_
    """
    if not isinstance(numerator, int):
        raise TypeError("numerator must be an integer")

    if not isinstance(denominator, int):
        raise TypeError("denominator must be an integer")

    if denominator == 0:
        raise ValueError("denominator must be non-zero")

    return numerator / denominator

a = int(input("Enter a numerator: "))
b = int(input("Enter a denominator: "))
q = divide(a, b)
print("The quotient is", q)