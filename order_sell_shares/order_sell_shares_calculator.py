from order_buy_shares.order_buy_shares_calculator import order_shares_buy


def order_shares_sell() -> float:
    """
    Calcula el valor de una orden de venta a partir de las participaciones
    compradas y el precio de venta ingresado.

    Args:
        None: solicita el precio de venta mediante entrada estándar y recupera
        las participaciones a vender llamando a ``order_shares_buy``.

    Return:
        float: valor total de la orden de venta. Devuelve 0.0 si los datos
        ingresados no son válidos o no se registró una compra previa.
    """

    # Inicializa el acumulador de la venta.
    sell_calculator = 0.0
    # Obtiene la cantidad de participaciones compradas.
    order_shares = order_shares_buy()

    # Valida que exista una compra previa y que el precio de venta sea válido.
    if order_shares > 0:
        sell_price = float(input("Please, write the current price of sell: "))
        if sell_price > 0:
            sell_calculator = order_shares * sell_price
            print(f"The value of this sell order is: {sell_calculator:.2f}")
            return sell_calculator

    # Informa que no se pudieron calcular participaciones válidas.
    print("The value that you enter is not greather that 0.")
    return sell_calculator
