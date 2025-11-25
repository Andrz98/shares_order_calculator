# projects/tests/test_orders.py

from unittest.mock import patch

# Evita que los imports de los módulos pidan input al cargar
with patch("builtins.input", side_effect=["0"] * 10):
    from order_buy_shares import (
        list_of__buy_shares,
        order_buy_shares_calculator,
        total_buy_shares,
    )
    from order_sell_shares import (
        list_of_sell_shares,
        order_sell_shares_calculator,
        total_sell_shares,
    )


# ---------- TESTS COMPRA ----------


def test_order_shares_buy():
    # capital = 100, precio = 20 -> 5 participaciones
    with patch("builtins.input", side_effect=["100", "20"]):
        result = order_buy_shares_calculator.order_shares_buy()
    assert result == 5.0


def test_list_of_shares():
    # Simulamos dos compras: 1.5 y 2.5, luego respondemos "y" y "n"
    with patch(
        "order_buy_shares.list_of__buy_shares.order_shares_buy",
        side_effect=[1.5, 2.5],
    ):
        with patch("builtins.input", side_effect=["y", "n"]):
            result = list_of__buy_shares.list_of_shares()
    assert result == [1.5, 2.5]


def test_total_buy_shares_etf():
    # 1 + 2 + 3 = 6
    result = total_buy_shares.total_buy_shares_etf([1.0, 2.0, 3.0])
    assert result == 6.0


def test_shares_buy_etf_id():
    # Asigna IDs empezando en 1
    result = total_buy_shares.shares_buy_etf_id([10.0, 20.0])
    assert result == [(1, 10.0), (2, 20.0)]


# ---------- TESTS VENTA ----------


def test_order_shares_sell():
    # order_shares_buy -> 5 participaciones, precio venta = 10 -> 50
    with patch(
        "order_sell_shares.order_sell_shares_calculator.order_shares_buy",
        return_value=5.0,
    ):
        with patch("builtins.input", side_effect=["10"]):
            result = order_sell_shares_calculator.order_shares_sell()
    assert result == 50.0


def test_total_sell_shares_list():
    # Simulamos dos órdenes de venta: 100 y 50, luego "y" y "n"
    with patch(
        "order_sell_shares.list_of_sell_shares.order_shares_sell",
        side_effect=[100.0, 50.0],
    ):
        with patch("builtins.input", side_effect=["y", "n"]):
            result = list_of_sell_shares.total_sell_shares()
    assert result == [100.0, 50.0]


def test_total_sell_shares_etf():
    # 100 + 50 = 150
    result = total_sell_shares.total_sell_shares_etf([100.0, 50.0])
    assert result == 150.0


def test_share_sell_etf_id():
    # Asigna IDs empezando en 1
    result = total_sell_shares.share_sell_etf_id([100.0, 50.0])
    assert result == [(1, 100.0), (2, 50.0)]
