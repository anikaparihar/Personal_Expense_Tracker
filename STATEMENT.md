**Project Statement: Personal Expense Tracker**

**Problem Statement**

Tracking personal finances can be challenging and often leads to confusion about where money is actually being spent. This lack of insight hinders effective budgeting and saving. This project aims to simplify expense logging and provide actionable analytics to help users gain clarity over their spending.

**Scope of the Project**

The project is a **Command Line Interface (CLI)** application built in Python. Its scope is focused on providing a **robust and reliable** solution for managing expense data using modular programming principles. It exclusively handles **CRUD** operations and data analysis. The application uses a simple CSV file for data persistence, ensuring an offline and portable solution.

**Target Users**

**Students** or **individuals** who need a lightweight, quick-entry tool for tracking daily spending.

Users who are comfortable with text-based interfaces and require a simple, reliable, and offline financial tool.

**High-Level Features (Functional Modules)**

**Record Management (Create, Update, Delete):**

Allows users to add new expense records with validated input (Date, Amount).

Enables editing and deleting existing records using their unique ID.

**Data Persistence & Reliability:**

Automatically loads data upon startup and saves all changes back to a persistent expenses.csv file upon exit or after any modification.

**Advanced Reporting & Analytics (Read/Analytics):**

**Category Summary:** Provides a total breakdown of spending across all categories.

**Time-Series Analysis:** Generates trend reports showing spending grouped by Week, Month, or Year, complete with a text-based bar chart for visualization.
