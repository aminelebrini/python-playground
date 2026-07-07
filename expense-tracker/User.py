from Expense import Expense

class User:
    def __init__(self, name):
        self.name = name
        self.expense = Expense()
    
    def add_expense(self, id, amount, category, date):
        self.expense.expenses.append({'id': id,'amount': amount, 'category': category, 'date': date})
    
    def remove_expenses(self, index):
        if self.expense.expenses.pop(index):
            return self.expense.expenses[index]
        else:
            return "Expense not found"

    def get_expenses(self):
        return self.expense.expenses
    
    
    def get_total_expenses(self):
        total = 0

        for expense in self.expense.expenses:
            total += expense['amount']
        return total
    
    def get_expenses_by_category(self, category):
        expenses_by_category = []
        for expense in self.expense.expenses:
            if expense['category'] == category:
                expenses_by_category.append(expense)
        return expenses_by_category

user = User("John Doe")
user.add_expense(1, 100, "Food", "2023-01-01")
user.add_expense(2, 50, "Transport", "2023-01-02")
print(user.get_total_expenses())
print(user.get_expenses_by_category("Food"))