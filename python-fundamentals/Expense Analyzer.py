# What is the total amount spent?
# What is the average expense?
# How much was spent in each category?
# Which category had the highest spending?
# Handle an empty list.

expenses = [
    {"category": "food", "amount": -50},
    {"category": "travel", "amount": 300}
]

def analyse(expenses):
    if not expenses:
        return None
    total_expense = 0
    category_expense = {}
    highest_amount = None
    highest_category = []

    for expense in expenses:
        if expense["amount"] is None or expense["amount"] < 0:
            return None
        total_expense += expense["amount"]
        category_expense[expense["category"]] = category_expense.get(expense["category"],0) + expense["amount"]
    
    for key in category_expense:
        if category_expense[key] == 0:
            continue
        elif highest_amount is None or category_expense[key] > highest_amount:
            highest_category.clear()
            highest_category.append(key)
            highest_amount = category_expense[key]
        elif category_expense[key] == highest_amount:
            highest_category.append(key)

    average_expense = total_expense/len(expenses)

    return {
        "total_spent":total_expense,
        "average_expense": average_expense,
        "category_expense": category_expense,
        "highest_category" : highest_category
    }

expense = analyse(expenses)

if expense is None:
    print('Provide correct data')
else:
    print('Your expense details: ',f'Total expense = {expense['total_spent']}', f'Average expense = {expense['average_expense']}','Category wise expense :',sep = "\n")
    for key in expense['category_expense']:
        print(f'{key}: {expense['category_expense'][key]}')
    if not expense['highest_category']:
        print('No highest category since you have spent 0')
    else:
        print('Category having the most expense =', end=' ')
        for i in expense['highest_category']:
            print(i, end=' ')
