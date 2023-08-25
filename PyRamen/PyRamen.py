import csv
from pathlib import Path

# Setting the file paths
menu_filepath = Path('menu_data.csv')
sales_filepath = Path('sales_data.csv')

# Reading and processing the menu data
menu = {}
with open(menu_filepath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        name, _, _, price, cost = row
        menu[name] = {"price": float(price), "cost": float(cost)}

# Reading and processing sales data
report = {}
with open(sales_filepath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    for row in reader:
        _, _, _, quantity, menu_item = row
        quantity = int(quantity)
        
        if menu_item in menu:
            if menu_item not in report:
                report[menu_item] = {'01-count': 0, '02 revenue': 0, '03-cogs': 0, '04-profit': 0}
                
            report[menu_item]['01-count'] += quantity
            report[menu_item]['02-revenue'] += menu[menu_item]['price'] * quantity
            report[menu_item]['03-cogs'] += menu[menu_item]['cost'] * quantity
            report[menu_item]['04-profit'] += (menu[menu_item]['price'] - menu[menu_item]['cost']) * quantity

# Writing the report to a text file
with open("report.txt", "w") as file:
    for key, value in report.items():
        file.write(f"{key} {value}\n")
        print("Report printed!"}
