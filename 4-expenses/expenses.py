"""
    Создать список из трат за неделю (7 чисел)
    Посчитать сумму, среднее, минимум и максимум.
    Сохранить в кортеже (минимум, максимум, сумма) и вывести его.
"""

expense_list = [30, 890, 57, 365, 439, 1009, 45]
expenses_sum = sum(expense_list)
average_daily = expenses_sum / len(expense_list)
max_expense = max(expense_list)
min_expense = min(expense_list)

balance = (min_expense, max_expense, expenses_sum)
print(balance)