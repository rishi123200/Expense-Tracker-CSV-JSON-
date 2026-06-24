import csv
import json
import os

CSV_FILE = "expenses.csv"
JSON_FILE = "expenses.json"

def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    # Save to CSV
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    # Save to JSON
    expenses = []
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            try:
                expenses = json.load(file)
            except:
                expenses = []

    expenses.append(expense)

    with open(JSON_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

    print("Expense Added Successfully!")

def view_expenses():
    if not os.path.exists(CSV_FILE):
        print("No expenses found.")
        return

    print("\n----- Expense Records -----")
    total = 0

    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) == 3:
                print(f"Date: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]}")
                total += float(row[2])

    print("---------------------------")
    print("Total Expenses: ₹", total)

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")