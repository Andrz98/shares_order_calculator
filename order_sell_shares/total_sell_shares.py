def total_sell_shares_etf(order_sell_share_list: list[float]) -> float:
    total_sell_shares = 0.0

    for sell_calculator in order_sell_share_list:
        total_sell_shares = total_sell_shares + sell_calculator
    return total_sell_shares


def share_sell_etf_id(order_sell_share_list_id: list[float]):
    sell_share_with_id = []
    sell_share_id = 1

    for sell_calculator in order_sell_share_list_id:
        sell_share_with_id.append((sell_share_id, sell_calculator))
        sell_share_id += 1
    return sell_share_with_id
