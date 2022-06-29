from expenses_basic import Expense
from config import CURRENCY


def _get_formatted_expenses(expense: Expense) -> str:
    pattern = f"\nДата траты : {expense.date}" \
        f"\nТип траты : {expense.expense_type}" \
        f"\nСумма траты : {expense.price} {CURRENCY}" \
        f"\nНа что потратили : {expense.on_what_spent}"
    return pattern


def print_expense(expense: Expense) -> None:
    print(_get_formatted_expenses(expense))
