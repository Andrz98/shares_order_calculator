def total_buy_shares_etf(order_shares_list: list[float]) -> float:
    """
    Devuelve el total de participaciones acumuladas en:
    ETF: Core S&P 500 USD (Acc)

    Args:
        order_shares_list (list[float]): Número de participaciones
        acumuladas en una lista.
        order_shares (float): Número de particiones compradas
        en la nueva operación (capital)

    Return:
        total_shares (float): nuevo total de participaciones acumuladas
    """
    total_shares = 0.0
    for order_shares in order_shares_list:
        total_shares = total_shares + order_shares
    return total_shares


def shares_buy_etf_id(order_share_list_id: list[float]):
    shares_with_id = []
    share_id = 1

    for order_shares in order_share_list_id:
        shares_with_id.append((share_id, order_shares))
        share_id += 1
    return shares_with_id
