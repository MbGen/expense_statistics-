import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import peewee

from datetime import datetime
from typing import NamedTuple, Iterable, Any, Literal
from enum import Enum

from expenses_saver import ExpenseModel
from config import CURRENCY


sns.set_theme(style="whitegrid", palette="pastel")


class ExpenseField(Enum):
    Date = "date"
    Type = "expense_type"
    Price = "price"
    Spent = "spent"


class DateLimit(NamedTuple):
    begin_date: datetime
    end_date: datetime


def _show_bar_plot(*,
                   dataframe: pd.DataFrame = None,
                   x: ExpenseField = None,
                   y: ExpenseField = None,
                   title: str = None,
                   show_spent: bool = False) -> None:
    res = sns.barplot(x=x.value, y=y.value, data=dataframe)
    TITLE_OFFSET = 1.1
    for bars in res.containers:
        if show_spent:
            res.bar_label(bars, labels=[f"{row.price} {CURRENCY}\n{row.spent}" for _, row in dataframe.iterrows()])
        else:
            res.bar_label(bars)
    res.set_title(title, y=TITLE_OFFSET)
    plt.show()


def _get_expenses_from_db(condition: peewee.Expression = None) -> peewee.ModelSelect:
    if condition is None:
        return (ExpenseModel
                .select()
                .order_by(ExpenseModel.date).dicts())
    return (ExpenseModel
            .select()
            .order_by(ExpenseModel.date)
            .where(condition).dicts())


def all_expenses(date_limit: DateLimit = None) -> None:
    """Shows bar plot with entire expenses"""
    if date_limit is None:
        _show_expenses_by_price(_get_expenses_from_db(), ExpenseField.Date)
    else:
        _show_expenses_by_price(_get_expenses_from_db((ExpenseModel.date >= date_limit.begin_date) &
                                                      (ExpenseModel.date <= date_limit.end_date)), ExpenseField.Date)


def average_expenses(date_limit: DateLimit = None) -> None:
    """Shows bar plot with average expenses"""
    if date_limit is None:
        _show_average_expenses(_get_expenses_from_db(), ExpenseField.Type)
    else:
        _show_average_expenses(_get_expenses_from_db((ExpenseModel.date >= date_limit.begin_date) &
                                                     (ExpenseModel.date <= date_limit.end_date)), ExpenseField.Type)


def min_expenses(date_limit: DateLimit = None) -> None:
    """Shows bar plot with min expenses"""
    if date_limit is None:
        _show_min_expenses(_get_expenses_from_db(), ExpenseField.Type)
    else:
        _show_min_expenses(_get_expenses_from_db((ExpenseModel.date >= date_limit.begin_date) &
                                                 (ExpenseModel.date <= date_limit.end_date)), ExpenseField.Type)


def max_expenses(date_limit: DateLimit = None) -> None:
    if date_limit is None:
        _show_max_expenses(_get_expenses_from_db(), ExpenseField.Type)
    else:
        _show_max_expenses(_get_expenses_from_db((ExpenseModel.date >= date_limit.begin_date) &
                                                 (ExpenseModel.date <= date_limit.end_date)), ExpenseField.Type)


def _show_expenses_by_price(expenses: Iterable[Any],
                            field: Literal[ExpenseField.Date, ExpenseField.Type]) -> None:
    dataframe = pd.DataFrame(expenses)
    dataframe = pd.DataFrame(dataframe.groupby(field.value)[ExpenseField.Price.value].sum()).reset_index()
    _show_bar_plot(dataframe=dataframe, x=field, y=ExpenseField.Price, title="Все расходы")


def _show_average_expenses(expenses: Iterable[Any],
                           field: Literal[ExpenseField.Date, ExpenseField.Type]) -> None:
    dataframe = pd.DataFrame(expenses)
    mean_dataframe = pd.DataFrame(dataframe.groupby(field.value)[ExpenseField.Price.value].mean()).reset_index()
    _show_bar_plot(dataframe=mean_dataframe, x=field, y=ExpenseField.Price, title="Расходы в среднем")


def _show_min_expenses(expenses: Iterable[Any],
                       field: Literal[ExpenseField.Date, ExpenseField.Type]) -> None:
    dataframe = pd.DataFrame(expenses)
    dataframe = dataframe.loc[dataframe.groupby(field.value)[ExpenseField.Price.value].idxmin()]
    _show_bar_plot(dataframe=dataframe,
                   x=field,
                   y=ExpenseField.Price,
                   title="Минимальные расходы",
                   show_spent=True)


def _show_max_expenses(expenses: Iterable[Any],
                       field: Literal[ExpenseField.Date, ExpenseField.Type]) -> None:
    dataframe = pd.DataFrame(expenses)
    dataframe = dataframe.loc[dataframe.groupby(field.value)[ExpenseField.Price.value].idxmax()]
    _show_bar_plot(dataframe=dataframe,
                   x=field,
                   y=ExpenseField.Price,
                   title="Маскимальные расходы",
                   show_spent=True)


if __name__ == "__main__":
    min_expenses()
