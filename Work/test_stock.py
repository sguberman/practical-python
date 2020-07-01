# test_stock.py

import pytest
import stock


def test_create():
    s = stock.Stock('GOOG', 100, 490.1)
    assert s.name == 'GOOG'
    assert s.shares == 100
    assert s.price == 490.1


def test_cost():
    s = stock.Stock('GOOG', 100, 490.1)
    assert s.cost == 49010.0


def test_sell():
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(1)
    assert s.shares == 99


def test_shares_type():
    s = stock.Stock('GOOG', 100, 490.1)
    with pytest.raises(TypeError):
        s.shares = '100'
