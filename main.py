from order_buy_shares.list_of__buy_shares import list_of_shares
from order_buy_shares.total_buy_shares import (
    shares_buy_etf_id,
    total_buy_shares_etf,
)
from order_sell_shares.list_of_sell_shares import total_sell_shares
from order_sell_shares.total_sell_shares import share_sell_etf_id

# 1) Construyes la lista con todas las órdenes
order_shares_list = list_of_shares()
order_sell_share_list = total_sell_shares()

# 2) Calculas el total de participaciones
total_buy = total_buy_shares_etf(order_shares_list)
print(f"Your total ETF shares are: {total_buy:.2f}")
total_sells = total_sell_shares()  # Posible error ¿Algún argumento?
print(f"Your total ETF sell shares are: {total_sells:.2f}")


# 3) Generas los IDs para cada orden
shares_with_id = shares_buy_etf_id(order_shares_list)

print("Detail of your ETF share orders (ID: shares): ")
for share_id, shares in shares_with_id:
    print(f"  ID {share_id}: {shares:.2f} shares")

formatted_orders = [
    f"ID {share_id}: {shares:.2f} shares" for share_id, shares in shares_with_id
]
print(formatted_orders)


sell_shares_with_id = share_sell_etf_id(order_sell_share_list)
print("Detail of your ETF share orders (ID: shares): ")
for sell_share_id, shares in sell_shares_with_id:
    print(f"  ID {sell_share_id}: {shares:.2f} shares")

formatted_sell_orders = [
    f"ID {share_id}: {shares:.2f} shares" for share_id, shares in shares_with_id
]
print(formatted_sell_orders)
