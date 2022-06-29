# Basic expenses logic #

## Configuration ##
**open config.py and set own params if you want**  
_default params_  
```python
DEFAULT_DB_NAME = "expenses.db" -> where expenses will be stored
DEFAULT_TIME_FORMAT = "%Y-%m-%d" -> see datetime docs to change time format
CURRENCY = "грн"
```


## Usage ##
**import datetime to be able set it on expense**  
``` python
from datetime import datetime
```
  
**import basic types to work with them**  
```python
from expenses_basic import Expense, ExpenseType
```

  
**import saver that saves expenses to database**  
```python
from expenses_saver import save_expense
```
  
**import expenses printer to see formated expenses in console**  
```python
from expenses_printer import print_expense
```
  
**import expenses statistic to see graphs**  
```python
from expenses_statistic import all_expenses, average_expenses, min_expenses, max_expenses
```
  
## Example ##
```python
def main():
     expense = Expense(
 	    date=datetime.now(),
 	    expense_type=ExpensesType.Other,
 	    price=2983.23,
 	    on_what_spent="milk"
     )
     save_expense(expense)
     print_expense(expense)
     all_expenses()  # Show plot with all expenses see func docs to manage dates
 
 
 if __name__ == __main__:
     main()
```
