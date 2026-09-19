# cosc310-lecture2

Lecture 2 exercises — Python & Git.

## Contents

| File | What it does |
|---|---|
| `exercise1.py` | Loads `data/menu.json` and prints available items under $10, cheapest first. |
| `exercise2.py` | A `Cart` class: add/remove/clear lines and compute a total. |
| `exercise3.py` | The same `Cart`, with business rules enforced by the cart itself. |
| `tests/test_cart.py` | pytest suite covering totals, quantity merging, and each rejection. |

## Setup

```bash
python -m venv .venv          # python3 on macOS/Linux
.venv\Scripts\Activate.ps1    # source .venv/bin/activate on macOS/Linux
pip install -r requirements.txt
```

## Run

```bash
python exercise1.py
python exercise2.py
python exercise3.py
pytest -v
```

## Business rules

All three live in `Cart.add_item` / `Cart.remove_item` in `exercise3.py`, not in
any calling code:

- `ValueError` when `qty < 1`
- `OutOfStockError` when the item's `available` field is `False`
- `KeyError` when removing an item that is not in the cart

Validation runs before any mutation, so a rejected operation leaves the cart
unchanged.
