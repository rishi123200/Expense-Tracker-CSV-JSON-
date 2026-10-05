import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def get_valid_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ").strip()

        if len(date) == 10 and date[2] == "-" and date[5] == "-":
            day = date[:2]
            month = date[3:5]
            year = date[6:]

            if day.isdigit() and month.isdigit() and year.isdigit():
                day = int(day)
                month = int(month)
                year = int(year)

                if 1 <= month <= 12:
                    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                    if month == 2 and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
                        max_day = 29
                    else:
                        max_day = days[month - 1]

                    if 1 <= day <= max_day:
                        return date

        print("Invalid date. Please enter date in DD-MM-YYYY format.")


def get_valid_amount():
    while True:
        amount = input("Enter amount: ₹").strip()

        if amount.count(".") <= 1:
            check_amount = amount.replace(".", "", 1)

            if check_amount.isdigit() and amount != ".":
                amount = float(amount)

                if amount > 0:
                    return amount

        print("Invalid amount. Please enter a positive number.")


def add_expense():
    date = get_valid_date()

    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    amount = get_valid_amount()

    while True:
        description = input("Enter description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category.title(), amount, description])

    print("Expense added successfully!")


def view_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        rows = list(reader)

        if not rows:
            print("\nNo expenses found.")
            return

        print("\n" + "=" * 75)
        print(f"{'Date':<15}{'Category':<15}{'Amount':<15}{'Description':<30}")
        print("=" * 75)

        for row in rows:
            print(
                f"{row['Date']:<15}"
                f"{row['Category']:<15}"
                f"₹{float(row['Amount']):<14.2f}"
                f"{row['Description']:<30}"
            )

        print("=" * 75)


def calculate_total():
    total = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expense: ₹{total:.2f}")


def category_summary():
    category_expenses = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"].title()
            amount = float(row["Amount"])

            if category in category_expenses:
                category_expenses[category] += amount
            else:
                category_expenses[category] = amount

    if not category_expenses:
        print("\nNo expenses found.")
        return

    print("\n========== CATEGORY SUMMARY ==========")

    for category, amount in category_expenses.items():
        print(f"{category:<20} ₹{amount:.2f}")

    print("======================================")


def search_by_category():
    search_category = input("Enter category to search: ").strip().lower()

    if not search_category:
        print("Category cannot be empty.")
        return

    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Category"].strip().lower() == search_category:
                found = True

                print(
                    f"Date: {row['Date']} | "
                    f"Category: {row['Category']} | "
                    f"Amount: ₹{float(row['Amount']):.2f} | "
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

        choice = input("Enter your choice: ").strip()

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
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()