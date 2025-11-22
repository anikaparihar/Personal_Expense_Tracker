import data_io
import expense_crud
import analysis_report

# --- Main Program Logic (Logical Workflow) ---

def display_menu():
    """Prints the main menu options to the console (Usability NFR)."""
    print("\n" + "="*40)
    print("    PERSONAL EXPENSE TRACKER MENU")
    print("="*40)
    print("1. Add New Expense (CREATE)")
    print("2. View All Expenses (READ)")
    print("3. Generate Summary Report (ANALYTICS - Category)")
    print("4. Edit Expense (UPDATE)")
    print("5. Delete Expense (DELETE)")
    print("6. Generate Time-Series Report (ANALYTICS - Time)") # NEW OPTION, now 6
    print("7. Exit") # Now 7
    print("-" * 40)

def main_loop():
    """
    The main execution loop of the application.
    It loads data, runs the menu, and ensures data is saved upon exit.
    """
    # Load data once at startup
    expense_data = data_io.load_data()
    print("Welcome to the Expense Tracker!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip() # Input prompt updated

        # Handle user choice using conditional statements
        if choice == '1':
            # 1. Add New Expense (CREATE)
            expense_data = expense_crud.add_expense(expense_data)
        
        elif choice == '2':
            # 2. View All Expenses (READ)
            analysis_report.display_all_expenses(expense_data)
            
        elif choice == '3':
            # 3. Generate Summary Report (ANALYTICS - Category)
            analysis_report.display_summary_report(expense_data)

        elif choice == '6':
            # 6. Generate Time-Series Report (ANALYTICS - Time)
            analysis_report.display_time_series_report(expense_data)
            
        elif choice == '4':
            # 4. Edit Expense (UPDATE) - Must display records first
            analysis_report.display_all_expenses(expense_data)
            expense_data = expense_crud.edit_expense(expense_data)
            
        elif choice == '5':
            # 5. Delete Expense (DELETE) - Must display records first
            analysis_report.display_all_expenses(expense_data)
            expense_data = expense_crud.delete_expense(expense_data)
            
        elif choice == '7':
            # 7. Exit - Save data before quitting
            print("\nSaving final data and exiting. Goodbye!")
            data_io.save_data(expense_data)
            break
            
        else:
            print("⚠️ Invalid choice. Please enter a valid option from the menu.")
            
        # Ensure data is saved after every successful CUD operation (Reliability)
        data_io.save_data(expense_data)

if __name__ == "__main__":
    main_loop()