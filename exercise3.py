"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def _find_line(self, item_id: int) -> dict | None:
        """Return the existing line for `item_id`, or None if there isn't one."""
        for line in self.lines:
            if line["item_id"] == item_id:
                return line
        return None

    def add_item(self, item: dict, qty: int = 1) -> None:
        """Add `qty` of `item`. Validates FIRST, so a rejected add changes nothing."""
        if qty < 1:
            raise ValueError(f"Quantity must be at least 1, got {qty}.")
        if not item["available"]:
            raise OutOfStockError(f"{item['name']} is currently out of stock.")

        existing = self._find_line(item["id"])
        if existing is not None:
            existing["qty"] += qty
            return

        self.lines.append(
            {
                "item_id": item["id"],
                "name": item["name"],
                "price": item["price"],
                "qty": qty,
            }
        )

    def remove_item(self, item_id: int) -> None:
        """Remove the line for `item_id`, or raise KeyError if it isn't in the cart."""
        if self._find_line(item_id) is None:
            raise KeyError(f"Item {item_id} is not in the cart.")
        self.lines = [line for line in self.lines if line["item_id"] != item_id]

    def clear(self) -> None:
        """Empty the cart."""
        self.lines = []

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

    # Rule 1: quantity must be at least 1.
    try:
        cart.add_item(gyoza, 0)
    except ValueError as e:
        print(f"Rejected (bad quantity): {e}")

    # Rule 2: an unavailable item cannot be ordered.
    try:
        cart.add_item(miso, 1)
    except OutOfStockError as e:
        print(f"Rejected (out of stock): {e}")

    # Rule 3: you cannot remove something that was never added.
    try:
        cart.remove_item(999)
    except KeyError as e:
        # KeyError repr()s its message, so str(e) comes back quoted.
        print(f"Rejected (not in cart): {e.args[0]}")

    # And the happy path still works, with nothing left over from the rejections.
    cart.add_item(gyoza, 2)
    print(f"Accepted: {cart}")
