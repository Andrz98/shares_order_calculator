def order_shares_buy():
    """
    Está función, permite ingresar la cantidad de capital y el precio de compra
    del ETF, con esos dos inputs calculamos la participación que obtenemos.
    La order_share que se genera, se agrega a una lista de particiones,
    de esta forma sabremos cuales son las partciones que tenemos.
    """
    capital = float(input("Please, enter your capital to invest: "))
    buy_price = float(input("Please, write the current price of purchase: "))

    if capital > 0 and buy_price > 0:
        order_shares = capital / buy_price
        print(f"Your approximate shares are: {order_shares:.2f}")

    else:
        print("The value that you enter is not greather that 0.")

    return order_shares


order_shares_buy()
