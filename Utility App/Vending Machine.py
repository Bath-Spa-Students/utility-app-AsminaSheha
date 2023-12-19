import time
import random

# Initial cash and stock values
cash = 0
item_stocks = {'A1': 6, 'A2': 8, 'A3': 5, 'A4': 12, 'A5': 8,
               'B1': 7, 'B2': 5, 'B3': 8, 'B4': 5, 'B5': 19,
               'C1': 15, 'C2': 5, 'C3': 6, 'C4': 4, 'C5': 5,
               'D1': 5, 'D2': 13, 'D3': 7, 'D4': 5, 'D5': 9,
               'E1': 9, 'E2': 9, 'E3': 8, 'E4': 5, 'E5': 15}

# Nested dictionary to store item information, including categories
items = {
    'A1': {'Category': 'Chocolates', 'Product Name': 'KitKat bar', 'Price': 1.5},
    'A2': {'Category': 'Chocolates', 'Product Name': "M&M's", 'Price': 2.0},
    'A3': {'Category': 'Chocolates', 'Product Name': "Reese's Peanut Butter Cups", 'Price': 1.75},
    'A4': {'Category': 'Chocolates', 'Product Name': 'Snickers', 'Price': 2.5},
    'A5': {'Category': 'Chocolates', 'Product Name': 'Hershey\'s Milk Chocolate', 'Price': 2.25},

    'B1': {'Category': 'Drinks', 'Product Name': 'Water', 'Price': 1.25},
    'B2': {'Category': 'Drinks', 'Product Name': 'Iced Tea', 'Price': 3.0},
    'B3': {'Category': 'Drinks', 'Product Name': 'Juice', 'Price': 2.5},
    'B4': {'Category': 'Drinks', 'Product Name': 'Coffee', 'Price': 1.75},
    'B5': {'Category': 'Drinks', 'Product Name': 'Energy Drink', 'Price': 2.75},

    'C1': {'Category': 'Soft Drinks', 'Product Name': 'Coca Cola', 'Price': 2.0},
    'C2': {'Category': 'Soft Drinks', 'Product Name': 'Dr. Pepper', 'Price': 1.5},
    'C3': {'Category': 'Soft Drinks', 'Product Name': 'Fanta', 'Price': 2.25},
    'C4': {'Category': 'Soft Drinks', 'Product Name': 'Pepsi', 'Price': 2.75},
    'C5': {'Category': 'Soft Drinks', 'Product Name': 'Sprite', 'Price': 1.25},

    'D1': {'Category': 'Chips', 'Product Name': 'Doritos Nacho Cheese Chips', 'Price': 1.75},
    'D2': {'Category': 'Chips', 'Product Name': "Lay's Classic Potato Chips", 'Price': 2.25},
    'D3': {'Category': 'Chips', 'Product Name': 'Takis Fuego Chips', 'Price': 2.5},
    'D4': {'Category': 'Chips', 'Product Name': 'Pringles Sour Cream and Onion', 'Price': 1.5},
    'D5': {'Category': 'Chips', 'Product Name': 'Cheetos Crunchy', 'Price': 2.0},

    'E1': {'Category': 'Other Snacks', 'Product Name': 'Pretzels', 'Price': 1.25},
    'E2': {'Category': 'Other Snacks', 'Product Name': 'Popcorn', 'Price': 1.5},
    'E3': {'Category': 'Other Snacks', 'Product Name': 'Trail Mix', 'Price': 2.0},
    'E4': {'Category': 'Other Snacks', 'Product Name': 'Granola Bars', 'Price': 1.0},
    'E5': {'Category': 'Other Snacks', 'Product Name': 'Rice Cakes', 'Price': 1.75},
}


def display_list():
    categories = ['Chocolates', 'Drinks', 'Soft Drinks', 'Chips', 'Other Snacks']
    for category in categories:
        print("\n---------------------------------------------------------------------------------")
        print(f"\n{category}")
        for code, item_info in sorted(items.items()):
            if item_info['Category'] == category:
                print(f"\nItem Code: {code} | Product Name: {item_info['Product Name']} | Price: ${item_info['Price']}"
                      f" | Stock: {item_stocks[code]}")


def validate_selection(selection):
    return selection in items


def process_purchase(selection):
    global cash
    global item_stocks

    if item_stocks[selection] > 0 and cash >= items[selection]['Price']:
        recommended_item = get_recommendation(selection)
        print(f"\nOne {items[selection]['Product Name']} has been dispensed.")
        print(f"Enjoy your {items[selection]['Product Name']} with {items[recommended_item]['Product Name']}!")
        cash -= items[selection]['Price']
        item_stocks[selection] -= 1
        print(f"There are {item_stocks[selection]} {items[selection]['Product Name']} left in stock.")
    elif item_stocks[selection] <= 0:
        print("\nThis item is out of stock.")
    elif cash == 0 or cash < items[selection]['Price']:
        print("\nBalance is insufficient, item will not be dispensed.")
        insufficient = input("Do you want to add more coins or banknotes? Type 'yes' to continue or any key to skip: ")
        if insufficient.lower() == 'yes':
            cash2 = float(input("\nInsert coins or banknotes: $"))
            cash += cash2
    else:
        print("\nThis is not a valid item code.")


def get_recommendation(selection):
    category = items[selection]['Category']
    other_items = [code for code, item_info in items.items() if item_info['Category'] == category and code != selection]
    return random.choice(other_items)


def purchasing_process():
    global cash
    global item_stocks

    print("\nWelcome to Asmina's Vending Machine!")

    display_list()

    print("\n---------------------------------------------------------------------------------")
    time.sleep(1)
    cash2 = float(input("\nInsert coins or banknotes: $"))
    cash += cash2

    selection_active = True
    while selection_active:
        print("\nYour balance is now $" + str(cash))
        selection = input("Enter the code of the item you would like to purchase: ")

        if validate_selection(selection):
            process_purchase(selection)
        else:
            print("This is not a valid item code.")

        repeat = input("\nWould you like to continue buying items? Type any key to continue or 'no' to quit: ")
        if repeat.lower() == 'no':
            selection_active = False
            print("\nYour total change is $" + str(cash))
            print("Thank you for buying from Asmina's Vending Machine!")


purchasing_process()
