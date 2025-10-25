"""
Inventory management system for tracking stock items.

This module provides functions to add, remove, and query inventory items.
"""

import json
from datetime import datetime

stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to the inventory with specified quantity."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    timestamp = str(datetime.now())
    logs.append(f"{timestamp}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove an item from the inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass


def get_qty(item):
    """Get the quantity of a specific item."""
    return stock_data[item]


def load_data():
    """Load inventory data from JSON file."""
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def save_data():
    """Save inventory data to JSON file."""
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(stock_data, f)


def print_data():
    """Print all items in the inventory."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Check items below threshold and return list."""
    result = []
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    apple_qty = get_qty("apple")
    print("Apple stock:", apple_qty)
    low_items = check_low_items()
    print("Low items:", low_items)
    save_data()
    print_data()
    # eval("print('eval used')")  # dangerous



main()
