def validate_symbol(symbol):

    if not symbol:
        raise ValueError("Symbol is required")

    return True



def validate_side(side):

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    return True



def validate_quantity(quantity):

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    return True