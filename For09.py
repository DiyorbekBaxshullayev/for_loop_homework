def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    x=[]
    a=price
    for i in range(1,11):
        x.append(price)
        price += a
    
    return x

print(main(2.25))
