import sqlite3

#_____________________________________________________________________

def setup_database():
    Connection = sqlite3.connect("store_inventory.db")

    cursor = Connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            reorder_threshold INTEGER NOT NULL
        )
    ''')
    Connection.commit()

    Connection.close()
#_____________________________________________________________________

def add_item():
    Connection = sqlite3.connect("store_inventory.db")

    cursor = Connection.cursor()

    item_name = input("What is the item name?")

    quantity = int(input("How many items are in stock?"))

    reorder_threshold = int(input("What is the safety number?"))

    cursor.execute('''
    INSERT INTO inventory(item_name, quantity, reorder_threshold)
    VALUES(?,?,?)
     ''', (item_name, quantity,reorder_threshold) )
    
    Connection.commit()

    Connection.close()
#_____________________________________________________________________

def view_all_stock():
    Connection = sqlite3.connect("store_inventory.db")

    cursor = Connection.cursor()

    cursor.execute("SELECT * FROM inventory")
    
    all_items = cursor.fetchall()

    for item in all_items:
        print(f"ID:{item[0]} | Name: {item[1]} | Stock: {item[2]}")

    Connection.close()

#_____________________________________________________________________

def update_item_stock():

    Connection = sqlite3.connect("store_inventory.db")

    cursor = Connection.cursor()

    id_Num = int(input("What number do you want to update?"))

    new_stock_Quantity = int(input("What is the new stock number?"))

    cursor.execute('''
    UPDATE inventory
    SET quantity = ?
    WHERE id = ?
    ''', (new_stock_Quantity,id_Num))

    Connection.commit()

    Connection.close()

#_____________________________________________________________________
setup_database()

while True:

    print("\n--- Store inventory Menus---")

    print("1. View Inventory")

    print("2. Add Item")

    print("3. Update Stock")

    print("4. Exit")

    Choice = input("Choose an option").strip()

    if Choice == "1":
        view_all_stock()
    elif Choice == "2":
        add_item()
    
    elif Choice == "3":
        update_item_stock()
        
    elif Choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid option try again") 