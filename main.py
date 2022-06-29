from datetime import datetime

from expenses_basic import Expense, ExpensesType
from expenses_saver import save_expense
from expenses_printer import print_expense
from analyse_expenses import all_expenses


def main():
    expense = Expense(
        date=datetime.now(),
        expense_type=ExpensesType.Other,
        price=32.2,
        on_what_spent="Мачку пасла"
    )
    print_expense(expense)


if __name__ == '__main__':
    main()
