# Ввести три траты: еда, транспорт, развлечения. Вывести общую сумму и среднее.
food : int = int(input("Введите сумму трат на еду: "))
transport : int = int(input("Введите сумму трат на транспорт: "))
entertainment : int = int(input("Введите сумму трат на развлечения: "))

sum = food + transport + entertainment
avg = sum / 3

print(f"Вы потратили всего: {sum}рублей")
print(f"В среднем вы потратили: {avg}рублей")