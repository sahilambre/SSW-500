# # Import necessary libraries
# import tkinter as tk
# import matplotlib.pyplot as plt

# # Define global variables
# expenses = []

# # Define functions for buttons
# def add_expense():
#     amount = float(amount_entry.get())
#     category = category_entry.get()
#     expenses.append((category, amount))
#     amount_entry.delete(0, tk.END)
#     category_entry.delete(0, tk.END)

# def delete_expense():
#     index = int(delete_entry.get())
#     expenses.pop(index-1)
#     delete_entry.delete(0, tk.END)

# def view_expenses():
#     expenses_window = tk.Toplevel(root)
#     for i, expense in enumerate(expenses):
#         category, amount = expense
#         tk.Label(expenses_window, text=f"{i+1}. {category}: {amount}").pack()

# def plot_expenses():
#     categories = [expense[0] for expense in expenses]
#     amounts = [expense[1] for expense in expenses]
#     plt.bar(categories, amounts)
#     plt.show()

# # Define main window
# root = tk.Tk()
# root.title("Expense Tracker")

# # Add widgets to main window
# tk.Label(root, text="Amount:").grid(row=0, column=0)
# amount_entry = tk.Entry(root)
# amount_entry.grid(row=0, column=1)

# tk.Label(root, text="Category:").grid(row=1, column=0)
# category_entry = tk.Entry(root)
# category_entry.grid(row=1, column=1)

# add_button = tk.Button(root, text="Add Expense", command=add_expense)
# add_button.grid(row=2, column=0)

# tk.Label(root, text="Delete Expense (Enter index):").grid(row=3, column=0)
# delete_entry = tk.Entry(root)
# delete_entry.grid(row=3, column=1)

# delete_button = tk.Button(root, text="Delete Expense", command=delete_expense)
# delete_button.grid(row=4, column=0)

# view_button = tk.Button(root, text="View Expenses", command=view_expenses)
# view_button.grid(row=4, column=1)

# plot_button = tk.Button(root, text="Plot Expenses", command=plot_expenses)
# plot_button.grid(row=5, column=0)

# root.mainloop()



#! Pyqt
# Import necessary libraries
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit
import matplotlib.pyplot as plt

# Define global variables
expenses = []

# Define main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expense Tracker")

        # Create input widgets
        self.amount_label = QLabel("Amount:", self)
        self.amount_label.move(50, 50)
        self.amount_entry = QLineEdit(self)
        self.amount_entry.move(120, 50)

        self.category_label = QLabel("Category:", self)
        self.category_label.move(50, 80)
        self.category_entry = QLineEdit(self)
        self.category_entry.move(120, 80)

        # Create buttons
        self.add_button = QPushButton("Add Expense", self)
        self.add_button.move(50, 120)
        self.add_button.clicked.connect(self.add_expense)

        self.delete_label = QLabel("Delete Expense (Enter index):", self)
        self.delete_label.move(50, 160)
        self.delete_entry = QLineEdit(self)
        self.delete_entry.move(200, 160)

        self.delete_button = QPushButton("Delete Expense", self)
        self.delete_button.move(50, 200)
        self.delete_button.clicked.connect(self.delete_expense)

        self.view_button = QPushButton("View Expenses", self)
        self.view_button.move(50, 240)
        self.view_button.clicked.connect(self.view_expenses)

        self.plot_button = QPushButton("Plot Expenses", self)
        self.plot_button.move(50, 280)
        self.plot_button.clicked.connect(self.plot_expenses)

        # Create text widget for displaying expenses
        self.expenses_text = QTextEdit(self)
        self.expenses_text.setGeometry(300, 50, 250, 300)

    # Define functions for buttons
    def add_expense(self):
        amount = float(self.amount_entry.text())
        category = self.category_entry.text()
        expenses.append((category, amount))
        self.amount_entry.clear()
        self.category_entry.clear()

    def delete_expense(self):
        index = int(self.delete_entry.text())
        expenses.pop(index-1)
        self.delete_entry.clear()

    def view_expenses(self):
        self.expenses_text.clear()
        for i, expense in enumerate(expenses):
            category, amount = expense
            self.expenses_text.append(f"{i+1}. {category}: {amount}")

    def plot_expenses(self):
        categories = [expense[0] for expense in expenses]
        amounts = [expense[1] for expense in expenses]
        plt.bar(categories, amounts)
        plt.show()

# Define main function
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 600, 400)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
