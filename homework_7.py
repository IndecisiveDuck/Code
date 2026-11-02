def calculate_order_total(subtotal:float, discount_percentage:float, tax_rate:float)->float:
    """Calculates the total cost of an order

    Args:
        subtotal (float): the total of the order before tax
        discount_percentage (float): any discounting precentage
        tax_rate (float): the tax percentage that will be applied to the total cost

    Returns:
        float: The final cost of the order
    """
    if type(subtotal) ==  str or type(discount_percentage) == str or type(tax_rate) == str:
        return 0.0
    discount = subtotal * discount_percentage / 100
    sales_total = subtotal - discount
    tax = sales_total * tax_rate / 100
    return sales_total + tax


def is_palendrome(string: str) -> bool:
    """Checks if a string is a palendrom by lowercasing and removing spaces. Then it reverses it and checks if the reversal is the same as the original.

    Args:
        string (str): initial string

    Returns:
        bool: true if string is a palendrome.
    """
    string = string.replace(" ","").lower()
    return string == string[::-1]

print(is_palendrome("steve"))