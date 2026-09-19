"""Exercise 1: Menu filtering.

Load data/menu.json and print every AVAILABLE item under $10.00,
sorted by price, cheapest first.

Expected output shape:
    Green Tea            $3.25
    Iced Coffee          $4.25
    ...

Requirements:
  - use an f-string for the output
  - type-hint every function you write
"""

import json
from pathlib import Path

MENU_PATH = Path(__file__).parent / "data" / "menu.json"


def load_menu() -> list[dict]:
    """Read the menu file and return it as a list of dictionaries."""
    with MENU_PATH.open() as f:
        return json.load(f)


def available_under(menu: list[dict], limit: float) -> list[dict]:
    """Return available items priced below `limit`, sorted cheapest first."""
    affordable = [
        item
        for item in menu
        if item["available"] and item["price"] < limit
    ]
    return sorted(affordable, key=lambda item: item["price"])


def format_line(item: dict) -> str:
    """Format one menu item as `name` left-padded to 20 chars, then the price."""
    return f"{item['name']:<20} ${item['price']:.2f}"


def main() -> None:
    menu = load_menu()
    for item in available_under(menu, 10.00):
        print(format_line(item))


if __name__ == "__main__":
    main()
