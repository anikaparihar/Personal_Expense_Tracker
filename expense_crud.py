from utilities import validate_positive_float, validate_date_format, get_next_id
from datetime import datetime # Added import for date validation in edit_expense

# Currency symbol constant (Matching analysis_report.py)
CURRENCY_SYMBOL = "₹"

# --- CRUD Functions (Functional Modules 1 & 3) ---

def add_expense(data):
    """
    FUNCTIONAL MODULE 1: Creates a new expense record.
    Prompts for input, validates it, and adds the new record to the list.
    """
    print("\n--- Add New Expense ---")
    
    # Use utility functions for validation (Error Handling)
    date = validate_date_format("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category (e.g., Food, Transport, Rent): ")
    amount = validate_positive_float(f"Enter Amount: {CURRENCY_SYMBOL}") # Currency updated here
    description = input("Enter Description: ")

    # Generate the next unique ID (Required for Update/Delete)
    new_id = get_next_id(data)
    
    # Create the new expense dictionary
    new_expense = {
        'ID': new_id,
        'Date': date,
        'Category': category.strip().capitalize(),
        'Amount': amount,
        'Description': description.strip()
    }
    
    data.append(new_expense)
    print(f"\n✅ Expense #{new_id} added successfully.")
    return data

def delete_expense(data):
    """
    FUNCTIONAL MODULE 3 (Delete): Prompts for an ID and removes the record.
    """
    if not data:
        print("💡 No expenses recorded to delete.")
        return data

    try:
        # User selects the ID to delete
        target_id = int(input("\nEnter the ID of the expense to DELETE: "))
    except ValueError:
        print("🚨 Error: ID must be a number.")
        return data

    # Find the index of the expense with the matching ID
    original_length = len(data)
    
    # Use a list comprehension to filter out the target expense
    new_data = [expense for expense in data if expense['ID'] != target_id]
    
    if len(new_data) < original_length:
        print(f"\n🗑️ Expense #{target_id} deleted successfully.")
        return new_data
    else:
        print(f"⚠️ Expense with ID #{target_id} not found.")
        return data

def edit_expense(data):
    """
    FUNCTIONAL MODULE 3 (Update): Prompts for an ID and allows editing fields.
    """
    if not data:
        print("💡 No expenses recorded to edit.")
        return data

    try:
        target_id = int(input("\nEnter the ID of the expense to EDIT: "))
    except ValueError:
        print("🚨 Error: ID must be a number.")
        return data

    # Find the expense dictionary to edit
    expense_to_edit = next((expense for expense in data if expense['ID'] == target_id), None)

    if expense_to_edit is None:
        print(f"⚠️ Expense with ID #{target_id} not found.")
        return data
    
    print(f"\n--- Editing Expense #{target_id} ---")
    
    # --- 1. Edit Date (FIXED LOGIC) ---
    current_date = expense_to_edit['Date']
    print(f"Current Date: {current_date}")
    
    # Use a loop to validate new date input
    while True:
        new_date_str = input("Enter new date (YYYY-MM-DD) or press Enter to skip: ")
        if not new_date_str:
            # User skipped editing the date
            break
        
        try:
            # Check validation without prompting again (using datetime.strptime directly)
            datetime.strptime(new_date_str, '%Y-%m-%d')
            expense_to_edit['Date'] = new_date_str
            break
        except ValueError:
            print("🚨 Error: Date format is invalid. Please use YYYY-MM-DD.")


    # 2. Edit Category
    current_category = expense_to_edit['Category']
    new_category = input(f"Current Category ({current_category}). Enter new category or press Enter to skip: ")
    if new_category:
        expense_to_edit['Category'] = new_category.strip().capitalize()

    # 3. Edit Amount
    current_amount = expense_to_edit['Amount']
    # Currency updated here
    new_amount_str = input(f"Current Amount ({CURRENCY_SYMBOL}{current_amount:.2f}). Enter new amount or press Enter to skip: ")
    if new_amount_str:
        try:
            validated_amount = float(new_amount_str)
            if validated_amount <= 0:
                 print("🚨 Error: Amount must be positive. Not updating amount.")
            else:
                expense_to_edit['Amount'] = validated_amount
        except ValueError:
            print("🚨 Error: Invalid input for amount. Not updating amount.")

    # 4. Edit Description
    current_desc = expense_to_edit['Description']
    new_description = input(f"Current Description ({current_desc}). Enter new description or press Enter to skip: ")
    if new_description:
        expense_to_edit['Description'] = new_description.strip()
        
    print(f"\n👍 Expense #{target_id} updated successfully.")
    return data