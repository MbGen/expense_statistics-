from enum import Enum
from typing import NamedTuple
from datetime import datetime


class ExpensesType(Enum):
    # Necessary expenses
    Tax = "Налог"

    # Internet expenses
    OnlineSubscriptions = "Онлайн подписки"

    # Other
    Other = "Другие"


class Expense(NamedTuple):
    date: datetime
    expense_type: ExpensesType
    price: float
    on_what_spent: str
