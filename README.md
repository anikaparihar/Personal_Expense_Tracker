**Personal Expense Tracker (CLI)**

A modular command-line interface (CLI) application built in Python for tracking, managing, and analyzing personal spending data. The application prioritizes reliability, maintainability, and clear reporting.

**Key Features & Functional Modules**
| Module | Feature | Description |
| :--- | :--- | :--- |
| **Data Management (CRUD)** | **Add, Edit, Delete** | Allows users to create new expense records, modify existing ones by ID, or remove records completely. |
| **Data Persistence** | **CSV File I/O** | All expense data is reliably loaded from and saved to a local `expenses.csv` file, ensuring data integrity across sessions. |
| **Analytics & Reporting** | **Summary Report** | Generates a breakdown of total spending grouped by Category, providing immediate insights into spending habits. |
| **Analytics & Reporting** | **Time-Series Report (NEW)** | Analyzes spending trends over time, providing summarized totals and a text-based bar chart grouped by **Week**, **Month**, or **Year**. |
| **Reliability** | **Input Validation** | Uses dedicated utility functions to validate user input for Amount (must be positive) and Date (must be in YYYY-MM-DD format), preventing data corruption. |

**Technologies Used**

**Language**: Python 3.x

**Libraries:** csv, datetime, operator, collections (all standard Python libraries)

**Data Storage:** CSV File

**Non-Functional Requirements**

**Reliability:** Validates user input and handles file exceptions to ensure every expense record is correct and persistent.

**Usability:** Simple CLI design with clear menus and instructions for all major workflows.

**Maintainability:** Modular file structure with each file addressing a single component of the larger system.

**Performance:** Efficiently manages thousands of records; operations are optimized for typical use cases.

**Portability:** Works with Python 3.x out of the box, without extra dependencies.

**Security:** Data is local and not transmitted online, ensuring privacy.

**Design Overview**
**Module Interaction**
flowchart TD
    Main[main.py] --> CRUD[expense_crud.py]
    Main --> IO[data_io.py]
    Main --> Analytics[analysis_report.py]
    Main --> Utils[utilities.py]
    CRUD --> IO
    Analytics --> IO
    
*Functional relationships between major modules.*

**Setup and Running Instructions**

**Project Setup:** Ensure all project files (main.py, data_io.py, expense_crud.py, analysis_report.py, utilities.py) are saved in the same directory.

**Data File:** Create an empty file named expenses.csv in the same directory.

**Run the Application:** Open your terminal or command prompt in the project directory and execute:

py main.py


*(Use python main.py if py does not work.)*

**Instructions for Testing**

To confirm the application works correctly, follow these steps:

Test 1: Create **(Input Validation)**

Select option 1 **(Add New Expense).**

Attempt to enter an invalid amount (e.g., -10 or abc). Verify the system prompts for re-entry until a valid positive number is entered.

Enter a new expense (Date: 2025-11-01, Category: Food, Amount: 500).

Test 2: Read & Persistence

Select option **2 (View All Expenses).** Verify the newly entered record is displayed.

Select option **7 (Exit)**, then immediately restart the application (py main.py).

Select option **2** again. The data must persist and still be displayed.

Test 3: Update & Delete

Select option **4 (Edit Expense)**. Enter the ID of the expense you just created (should be 1). Change the amount.

Select option **5 (Delete Expense)**. Enter the ID (1). Verify the record is successfully removed (check option 2).

Test 4: Analytics

Add at least five different expenses across different categories (e.g., Food, Rent, Transport) and different dates (e.g., 2025-10-15, 2025-11-01, 2025-11-15).

Select option **3 (Generate Summary Report)**. Verify the category totals and grand total are correct.

Select option **6 (Generate Time-Series Report)**. Test grouping by W, M, and Y and verify the output is sensible.

**Enhanced Error Handling**
Expense CSV loading now skips malformed or incomplete records and gives feedback, ensuring robust long-term performance.

**Potential Enhancements**
Support for recurring expenses or income

Exporting reports to PDF or Excel

Password protection and file encryption for greater privacy

A graphical (GUI) version of the app
