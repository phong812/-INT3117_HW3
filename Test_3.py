import pytest
import Main
def test_01():
    assert Main.Calculate_ticket_price(15, 150, 10000) == -1
def test_02():
    assert Main.Calculate_ticket_price(18, 135, 100000) == 70000
def test_03():
    assert Main.Calculate_ticket_price(18, 150, 110000) == 88000
def test_04():
    assert Main.Calculate_ticket_price(30, 120, 120000) == 102000
def test_05():
    assert Main.Calculate_ticket_price(35, 170, 150000) == 150000
