def order_shares_buy() -> float:
    """
    Calcula el número aproximado de participaciones a comprar.

    Args:
        None: la función solicita el capital y el precio de compra
        mediante entrada estándar.

    Return:
        float: número de participaciones calculadas. Devuelve 0.0 si
        los valores ingresados no son mayores que cero.
    """

    # Solicita el capital disponible para invertir.
    capital = float(input("Please, enter your capital to invest: "))
    # Solicita el precio actual de compra del ETF.
    buy_price = float(input("Please, write the current price of purchase: "))

    # Valida que ambos valores sean positivos antes de calcular.
    if capital > 0 and buy_price > 0:
        order_shares = capital / buy_price
        print(f"Your approximate shares are: {order_shares:.2f}")
        return order_shares

    # Informa al usuario que los datos no son válidos.
    print("The value that you enter is not greather that 0.")
    return 0.0
