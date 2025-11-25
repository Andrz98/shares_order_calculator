from .order_buy_shares_calculator import order_shares_buy


def list_of_shares():
    order_shares_list = []
    while True:
        order_shares = order_shares_buy()

        if order_shares <= 0:
            print("This order was not added to the list.")
        else:
            order_shares_list.append(order_shares)
            formatted_order_shares_list = [f"{x:.2f}" for x in order_shares_list]
            print(f"Your number of shares is: {formatted_order_shares_list}")

        answer = input("Do you want to add another buy order?(y/n): ").strip().lower()
        if answer != "y":
            break

    return order_shares_list
