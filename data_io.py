import csv

# Define the file name and the header fields (Schema Design)
FILE_NAME = 'expenses.csv'
FIELD_NAMES = ['ID', 'Date', 'Category', 'Amount', 'Description']

# --- File Handling Functions (Reliability NFR) ---

def load_data():
    """
    Loads all expense records from the CSV file.
    Initializes the file with headers if it doesn't exist or is empty.
    Returns the data as a list of dictionaries.
    """
    data = []
    try:
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert ID and Amount fields to appropriate types for in-memory use
                row['ID'] = int(row['ID'])
                row['Amount'] = float(row['Amount'])
                data.append(row)
    except FileNotFoundError:
        # Create the file if it doesn't exist
        print(f"File '{FILE_NAME}' not found. Creating a new one...")
        save_data([]) # Save an empty list to create the file with headers
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        
    return data

def save_data(data):
    """
    Writes the entire list of expense dictionaries back to the CSV file.
    This overwrites the previous content (full data write/save).
    """
    try:
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader() # Write the header row
            
            # Ensure Amount is converted back to a string/serializable format for CSV
            serializable_data = [{k: str(v) for k, v in expense.items()} for expense in data]
            writer.writerows(serializable_data)
    except Exception as e:
        print(f"An error occurred while saving data: {e}")