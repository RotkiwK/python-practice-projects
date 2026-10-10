import csv
import os

def add_inventry(name, quantity, price):
    file_exist = os.path.exists("inventory.csv")
    with open ("inventory.csv","a",newline="") as f:
        fieldname = ["name","quantity","price"]
        writer = csv.DictWriter(f,fieldnames=fieldname)
        if not file_exist:
            writer.writeheader()
        writer.writerow({"name": name, "quantity":quantity, "price":price})



def view_invenitry():
    try:
        with open ("inventory.csv","r",newline="") as f:
            reader =csv.DictReader(f)
            for row in reader:
                print (row["name"], row["quantity"], row["price"])
    except FileNotFoundError:
        print ("no inventry yet")

def total_inventory_value():
    total = 0
    multiplied = 0
    try:
        with open ("inventory.csv", "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                multiplied = float(row["quantity"]) * float(row["price"])
                total = total + multiplied
    except FileNotFoundError:
        print("no inventory yet")
        pass
    return total


def main():
    while True:
        print ("1 add an item ")
        print ("2 view all items ")
        print ("3 total inventory value ")
        print ("4 break ")
        user_input = input("choose 1 to 4 ")
        if user_input == "1":
            name = input("input the name ")
            quantity = input("input the quantity")
            price = input("input the price ")
            add_inventry(name,quantity,price)
        elif user_input == "2":
            view_invenitry()
        elif user_input == "3":
            print(total_inventory_value())
        elif user_input == "4":
            break 
        else: 
            print ("wrong input")
main()