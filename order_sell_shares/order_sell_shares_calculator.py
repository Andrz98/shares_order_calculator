from order_buy_shares.order_buy_shares_calculator import order_shares_buy


def order_shares_sell():

    sell_calculator = 0.0
    order_shares = order_shares_buy()

    if order_shares > 0:
        sell_price = float(input("Please, write the current price of sell: "))
        if sell_price > 0:
            sell_calculator = order_shares * sell_price
            print(f"The value of this sell order is: {sell_calculator:.2f}")
    else:
        print("The value that you enter is not greather that 0.")

    return sell_calculator


order_shares_sell()
