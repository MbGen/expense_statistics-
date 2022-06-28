from expenses_basic import Expense
from lxml import etree as et
from typing import Iterable

from config import DEFAULT_ENCODING


def get_formatted_expenses(expense: Expense) -> str:
    pattern = f"Дата траты = {expense.date}" \
        f"Тип траты = {expense.expense_type}" \
        f"Сумма траты = {expense.price}" \
        f"На что потратили = {expense.on_what_spent}"
    return pattern
