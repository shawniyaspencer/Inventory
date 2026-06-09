# Inventory

A simple, interactive command-line application built in Python and SQLite3 to track store inventory levels and safety reorder thresholds.

## Features
**Setup Database:** Automatically initializes a localized database file and inventory table.
**Add Items:** Insert new items with custom stock quantities and safety/reorder numbers.
**View Stock:** Read and display all current inventory logs directly from the database.
**Update Inventory:** Modify stock numbers on demand using specific item IDs.

---

## Project Structure
**inventory.py** - The main Python script containing the database logic and interactive menu loop.
**store_inventory.db** The localized SQLite database file generated automatically on startup.

---

## How to Run
1. Open your terminal.
2. Run the program using Python:
   bash
   python3 inventory.py
