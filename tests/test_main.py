from app.shop import Shop
import datetime


def test_receipt_output(capsys):
    shop = Shop(
        name="Test Shop",
        location=[0.0, 0.0],
        products={"Apple": 3.00, "Bread": 2.00, "Milk": 6.00}
    )

    cart = {"Apple": 2, "Bread": 1, "Milk": 2}
    timestamp = datetime.datetime(2023, 1, 1, 12, 0, 0)

    total = shop.print_receipt("Bob", cart, timestamp=timestamp)
    captured = capsys.readouterr()

    assert total == 20.0
    assert "2023-01-01 12:00:00" in captured.out
    assert "2 x Apple @ $3.00 = $6.00" in captured.out
    assert "1 x Bread @ $2.00 = $2.00" in captured.out
    assert "2 x Milk @ $6.00 = $12.00" in captured.out
    assert "Total: $20.00" in captured.out
