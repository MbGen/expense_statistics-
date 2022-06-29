# Basic expenses logic #

## Configuration ##
**open config.py and set own params if you want**
_default params_
`
DEFAULT_DB_NAME = "expenses.db" -> where expenses will be stored
DEFAULT_TIME_FORMAT = "%Y-%m-%d" -> see datetime docs to change time format
CURRENCY = "грн"
`


## Usage ##
**import datetime to be able set it on expense**
`from datetime import datetime`

**import basic types to work with them**
`from expenses_basic import Expense, ExpenseType`

**import saver that saves expenses to database**
`from expenses_saver import save_expense`

**import expenses printer to see formated expenses in console**
`from expenses_printer import print_expense`

**import expenses statistic to see graphs**
`from expenses_statistic import all_expenses, average_expenses, min_expenses, max_expenses`

## Example ##
`
def main():
	expense = Expense(
		date=datetime.now(),
		expense_type=ExpensesType.Other,
		price=2983.23,
		on_what_spent="milk"
	)
	save_expense(expense)
	print_expense(expense)
	all_expenses
`