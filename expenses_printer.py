from expenses_basic import Expense


def _get_formatted_expenses(expense: Expense) -> str:
    pattern = f"Дата траты = {expense.date}" \
        f"Тип траты = {expense.expense_type}" \
        f"Сумма траты = {expense.price}" \
        f"На что потратили = {expense.on_what_spent}"
    return pattern


def print_expense(expense: Expense) -> None:
    print(_get_formatted_expenses(expense))
