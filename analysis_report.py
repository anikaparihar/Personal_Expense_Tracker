from operator import itemgetter
from datetime import datetime
from collections import defaultdict

# Currency symbol constant (Updated from $ to ₹)
CURRENCY_SYMBOL = "₹"

# --- Reporting Functions (Functional Module 2 - Read/Analytics) ---

def display_all_expenses(data):
    """
    Displays all expense records in a clear, formatted table.
    Sorts by Date for better readability.
    """
    if not data:
        print("\n💡 No expenses recorded yet.")
        return

    print("\n" + "="*70)
    print(f"{'ID':<4} | {'Date':<10} | {'Category':<15} | {'Amount':>10} | {'Description':<25}")
    print("="*70)

    # Sort data by Date before displaying (Optional, but improves Usability)
    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['Date'], '%Y-%m-%d'), reverse=True)

    for expense in sorted_data:
        # Format the amount to two decimal places, using ₹
        amount_str = f"{CURRENCY_SYMBOL}{expense['Amount']:,.2f}"
        
        # Use f-strings for clear column alignment
        print(f"{expense['ID']:<4} | {expense['Date']:<10} | {expense['Category']:<15} | {amount_str:>10} | {expense['Description']:<25.25}")
        
    print("="*70)

def display_summary_report(data):
    """
    Calculates and displays the Total Spending and the summary by Category (Analytics).
    """
    if not data:
        print("\n💡 Cannot generate report: No expenses recorded.")
        return

    # Calculate Total Spending
    total_spending = sum(expense['Amount'] for expense in data)
    
    # Calculate Summary by Category (Data Grouping/Analytics)
    category_totals = {}
    for expense in data:
        category = expense['Category']
        amount = expense['Amount']
        category_totals[category] = category_totals.get(category, 0) + amount

    # --- Display Report ---
    print("\n" + "="*40)
    print("      💸 EXPENSE SUMMARY REPORT 💸")
    print("="*40)
    
    # 1. Display Category Totals
    print("\n--- Spending By Category ---")
    
    # Sort categories by amount spent (optional, but good practice)
    sorted_categories = sorted(category_totals.items(), key=itemgetter(1), reverse=True)
    
    for category, total in sorted_categories:
        print(f"{category:<20}: {CURRENCY_SYMBOL}{total:,.2f}")

    # 2. Display Grand Total
    print("\n--- Grand Total ---")
    print(f"TOTAL SPENDING{':':<8} {CURRENCY_SYMBOL}{total_spending:,.2f}")
    print("="*40)


def display_time_series_report(data):
    """
    Generates a time-based report (Weekly, Monthly, Yearly) and displays a text-based bar chart.
    This function adds depth to the Analytics module.
    """
    if not data:
        print("\n💡 Cannot generate time-series report: No expenses recorded.")
        return
    
    print("\n" + "="*50)
    print("    📊 TIME-SERIES SPENDING ANALYSIS 📊")
    print("="*50)
    
    period = input("Analyze spending by (W)eek, (M)onth, or (Y)ear? ").strip().upper()
    
    if period not in ['W', 'M', 'Y']:
        print("⚠️ Invalid choice. Please select W, M, or Y.")
        return

    # Determine the grouping key based on user choice
    time_groups = defaultdict(float)
    
    for expense in data:
        try:
            date_obj = datetime.strptime(expense['Date'], '%Y-%m-%d')
            amount = expense['Amount']

            key = None
            if period == 'Y':
                # Group by Year
                key = str(date_obj.year)
            elif period == 'M':
                # Group by Year-Month (e.g., 2025-11)
                key = date_obj.strftime('%Y-%m')
            elif period == 'W':
                # Group by Year-Week Number (e.g., 2025-W47)
                # Week number format %W starts counting from Monday
                key = date_obj.strftime('%Y-W%W')
            
            if key:
                time_groups[key] += amount
                
        except ValueError:
            # Skip records with invalid date format (should be caught by validation on input)
            continue 

    if not time_groups:
        print("⚠️ No valid expenses found to generate a time-series report.")
        return

    # Convert dictionary to list of (label, amount) tuples and sort them
    report_data = sorted(time_groups.items(), key=itemgetter(0))

    # Calculate Max Amount for Scaling the Bar Chart
    max_amount = max(amount for _, amount in report_data)
    
    print(f"\n--- Spending Grouped by {'Year' if period == 'Y' else 'Month' if period == 'M' else 'Week'} ---")
    
    # Generate Text-Based Bar Chart
    MAX_BAR_LENGTH = 30 
    
    for label, amount in report_data:
        # Calculate the length of the bar proportional to the max amount
        bar_length = int((amount / max_amount) * MAX_BAR_LENGTH)
        bar = '█' * bar_length # Use a block character for a solid bar
        
        amount_str = f"{CURRENCY_SYMBOL}{amount:,.2f}"
        
        # Display the bar chart line
        print(f"{label:<10} | {bar:<{MAX_BAR_LENGTH}} {amount_str}")

    print("\n" + "="*50)