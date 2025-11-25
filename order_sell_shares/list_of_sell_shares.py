from order_sell_shares.order_sell_shares_calculator import order_shares_sell


def total_sell_shares():
    order_sell_share_list = []

    while True:
        sell_calculator = order_shares_sell()

        if sell_calculator <= 0:
            print("This order was not added to the list.")
        else:
            order_sell_share_list.append(sell_calculator)
            formatted_order_sell_share = [f"{x:.2f}" for x in order_sell_share_list]
            print(f"Your number of sell shares is: {formatted_order_sell_share}")

        answer = input("Do you want to add another sell order?(y/n): ").strip().lower()

        if answer != "y":
            break

    return order_sell_share_list
