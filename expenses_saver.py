from datetime import datetime
from peewee import SqliteDatabase, Model, AutoField, DateField, FloatField, TextField, IntegrityError
from expenses_basic import Expense, ExpensesType
from os.path import exists

from config import DEFAULT_DB_NAME

database = SqliteDatabase(DEFAULT_DB_NAME)


class BaseModel(Model):
    class Meta:
        database = database


class ExpenseModel(BaseModel):
    _id = AutoField()
    date = DateField()
    expense_type = TextField()
    price = FloatField()
    spent = TextField()


def save_expense(expense: Expense) -> None:
    _create_db_file_ifn()
    try:
        ExpenseModel.create(
            date=expense.date,
            expense_type=expense.expense_type.value,
            price=expense.price,
            spent=expense.on_what_spent)
    except IntegrityError:
        return


def _create_db_file_ifn() -> None:
    """Creates file .db if that not exist"""
    if not exists(DEFAULT_DB_NAME):
        open(DEFAULT_DB_NAME, "w")
        ExpenseModel.create_table()


if __name__ == '__main__':
    save_expense(Expense(date=datetime(2022, 6, 17),
                         expense_type=ExpensesType.OnlineSubscriptions,
                         price=1420,
                         on_what_spent="Google"))
