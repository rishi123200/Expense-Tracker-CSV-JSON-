import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: ₹"))
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n" + "=" * 75)
        print(f"{'Date':<15}{'Category':<15}{'Amount':<15}{'Description':<30}")
        print("=" * 75)

        for row in reader:
            print(
                f"{row['Date']:<15}"
                f"{row['Category']:<15}"
                f"₹{float(row['Amount']):<14.2f}"
                f"{row['Description']:<30}"
            )

        print("=" * 75)


def calculate_total():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expense: ₹{total:.2f}")


def category_summary():
    category_expenses = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"].title()
            amount = float(row["Amount"])

            if category in category_expenses:
                category_expenses[category] += amount
            else:
                category_expenses[category] = amount

    print("\n========== CATEGORY SUMMARY ==========")

    for category, amount in category_expenses.items():
        print(f"{category:<20} ₹{amount:.2f}")

    print("======================================")


def search_by_category():
    search_category = input("Enter category to search: ").lower()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            if row["Category"].lower() == search_category:
                found = True
                print(
                    f"Date: {row['Date']} | "
                    f"Category: {row['Category']} | "
                    f"Amount: ₹{row['Amount']} | "
                    f"Description: {row['Description']}"
                )

        if not found:
            print("No expenses found.")


def main():
    initialize_file()

    while True:
        print("\n================================")
        print("        EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Category Summary")
        print("5. Search by Category")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            search_by_category()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice.")


main()