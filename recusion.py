def sum(n: int) -> int:
    """Returns the sum of the numbers 1 to n

    Args:
        n (int): number

    Returns:
        int: The sum
    """
    if n == 1:
        return n
    return n + sum(n-1)

def main():
    print(sum(5))

main()