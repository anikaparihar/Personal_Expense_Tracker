import re
from datetime import datetime

# --- Utility Functions for Input Validation (Error Handling NFR) ---

def validate_positive_float(prompt):
    """
    Prompts the user for input and ensures it is a positive number (float).
    It loops until valid input is received.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("🚨 Error: Amount must be a positive number.")
                continue
            return value
        except ValueError:
            print("🚨 Error: Invalid input. Please enter a numerical value.")

def validate_date_format(prompt):
    """
    Prompts the user for a date and ensures it is in YYYY-MM-DD format.
    It loops until a valid date is received.
    """
    while True:
        date_str = input(prompt)
        try:
            # Attempt to parse the date string using the specified format
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("🚨 Error: Date format is invalid. Please use YYYY-MM-DD (e.g., 2025-11-20).")

def get_next_id(data):
    """
    Calculates the next unique ID for a new expense record.
    This is essential for the CRUD operations (Update/Delete).
    """
    if not data:
        return 1
    # Find the maximum ID currently in the data and add 1
    return max(int(expense.get('ID', 0)) for expense in data) + 1