# Personal Expense Tracker (CLI)

A modular command-line interface (CLI) application built in Python for tracking, managing, and analyzing personal spending data. The application prioritizes reliability, maintainability, and clear reporting.

## Key Features & Functional Modules

| Module                 | Feature                | Description                                                                             |
| :--------------------- | :--------------------- | :-------------------------------------------------------------------------------------- |
| Data Management (CRUD) | Add, Edit, Delete      | Create new expense records, modify existing ones by ID, or remove records completely.    |
| Data Persistence       | CSV File I/O           | All expense data is loaded from and saved to a local `expenses.csv` file for data integrity. |
| Analytics & Reporting  | Summary Report         | Generates a breakdown of total spending grouped by Category for spending insight.        |
| Analytics & Reporting  | Time-Series Report     | Analyzes spending trends with a text-based bar chart, grouped by Week, Month, or Year.   |
| Reliability            | Input Validation       | Uses utility functions to validate amounts (positive) and dates (YYYY-MM-DD) to prevent errors. |

## Technologies Used

- **Language:** Python 3.x
- **Libraries:** csv, datetime, operator, collections (all standard Python libraries)
- **Data Storage:** CSV File

## Non-Functional Requirements

- **Reliability:** Validates user input and handles file exceptions to ensure every expense record is correct and persistent.
- **Usability:** Simple CLI design with clear menus and instructions for all major workflows.
- **Maintainability:** Modular file structure with each file addressing a single component of the larger system.
- **Performance:** Efficiently manages thousands of records; operations are optimized for typical use cases.
- **Portability:** Works with Python 3.x out of the box, without extra dependencies.
- **Security:** Data is local and not transmitted online, ensuring privacy.

## Design Overview

### Module Interaction

flowchart TD
Main[main.py] --> CRUD[expense_crud.py]
Main --> IO[data_io.py]
Main --> Analytics[analysis_report.py]
Main --> Utils[utilities.py]
CRUD --> IO
Analytics --> IO

*Functional relationships between major modules.*

## Setup and Running Instructions

1. **Project Setup:** Place all project files (`main.py`, `data_io.py`, `expense_crud.py`, `analysis_report.py`, `utilities.py`) in the same folder.
2. **Data File:** Create an empty file called `expenses.csv` in this folder.
3. **Run the Application:** In your terminal, navigate to the project folder and execute:

py main.py

*(If `py` doesn’t work, use `python main.py` instead.)*

## Instructions for Testing

- **Test 1:** Add a new expense; try an invalid amount (like `-10` or `abc`). App should ask for re-entry. Enter a valid expense.
- **Test 2:** View all expenses. Check if your entry appears. Exit and run the app again; data must persist.
- **Test 3:** Edit the expense just added; update the amount. Delete it; verify removal.
- **Test 4:** Add five or more expenses across categories and dates. Generate a Summary Report for totals, and a Time-Series Report (grouped by Week, Month, Year) for trends.

## Enhanced Error Handling

Expense CSV loading now skips malformed or incomplete records and gives feedback, ensuring robust long-term performance.

## Potential Enhancements

- Support for recurring expenses or income
- Exporting reports to PDF or Excel
- Password protection and file encryption for greater privacy
- A graphical (GUI) version of the app
