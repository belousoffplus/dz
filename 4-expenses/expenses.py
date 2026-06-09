"""
Сделать функции:
- add_expense(expenses, value) — добавляет расход
- delete_expense(expenses, index) — удалить расход (1-based)
- get_total(expenses) — возвращает сумму
- get_average(expenses) — возвращает средний расход
- print_report(expenses) — печатает красивый отчёт

Вызывать все функции в меню. Расходы хранить в list
"""

def parse_rubles(text: str) -> float | None:
    """Возвращает сумму в рублях (float) или None, если формат неверен."""
    text = text.strip().lower()
    parts = text.split()

    if len(parts) == 2:
        rub_str, rub_unit = parts
        if rub_str.isdigit() and rub_unit == "руб":
            return float(int(rub_str))
    
    elif len(parts) == 4:
        rub_str, rub_unit, kop_str, kop_unit = parts
        if (rub_str.isdigit() and kop_str.isdigit() and
            rub_unit == "руб" and kop_unit == "коп"):
            rub = int(rub_str)
            kop = int(kop_str)
            if 0 <= kop <= 99:
                return float(rub) + kop / 100

    return None


def add_expense(expenses: list, value: float) -> bool:
    """Добавляет расход, возвращает True при успехе."""
    if value > 0:
        expenses.append(value)
        print(f"✅ Добавлен расход: {value:.2f} ₽")
        return True
    print("❌ Сумма должна быть положительной.")
    return False


def delete_expense(expenses: list, index: int) -> bool:
    """Удаляет расход по номеру (1-based). Возвращает True при успехе."""
    if 1 <= index <= len(expenses):
        expenses.pop(index - 1)
        print("✅ Расход удалён.")
        return True
    print("❌ Неверный номер.")
    return False


def get_total(expenses: list) -> float:
    """Возвращает сумму расходов."""
    return sum(expenses) if expenses else 0.0


def get_average(expenses: list) -> float:
    """Возвращает средний расход."""
    return sum(expenses) / len(expenses) if expenses else 0.0


def print_report(expenses: list) -> None:
    """Красиво печатает отчёт."""
    if not expenses:
        print("❗ Нет расходов.")
        return

    print("\n" + "=" * 30)
    print("📖 Отчёт о расходах")
    print("-" * 30)
    for i, exp in enumerate(expenses, start=1):
        rub = int(exp)
        kop = int(round((exp - rub) * 100))  # округляем, чтобы избежать 0.00000004
        print(f"{i:2}. {rub}.{kop:02d} ₽")
    print("-" * 30)
    print(f"💰 Сумма: {get_total(expenses):.2f} ₽")
    print(f"📊 Среднее: {get_average(expenses):.2f} ₽")
    print("=" * 30 + "\n")


def is_int(s: str) -> bool:
    """Проверяет, можно ли привести строку к int (без исключений)."""
    s = s.strip()
    if not s:
        return False
    return s.isdigit() or (s.startswith('-') and s[1:].isdigit())


menu = [
    "Добавить расход",
    "Показать все расходы",
    "Показать сумму и средний расход",
    "Удалить расход по номеру",
    "Выход"
]

expenses: list[float] = []

while True:
    # Вывод меню
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item}")

    user_input = input("Введите пункт меню: ").strip()

    # Проверка на пустой ввод
    if not user_input:
        print("❌ Введите число.\n")
        continue

    # Проверка, является ли ввод целым числом
    if not is_int(user_input):
        print("❌ Введите число.\n")
        continue

    num_menu = int(user_input)

    if num_menu == 1:
        user_input_value = input("Введите сумму (например: 100 руб или 100 руб 50 коп): ")
        value = parse_rubles(user_input_value)
        if value is not None:
            add_expense(expenses, value)
        else:
            print("❌ Некорректный формат суммы.\n")

    elif num_menu == 2:
        print_report(expenses)

    elif num_menu == 3:
        if not expenses:
            print("❗ Нет расходов.")
        else:
            print(f"💰 Сумма: {get_total(expenses):.2f} ₽")
            print(f"📊 Среднее: {get_average(expenses):.2f} ₽\n")

    elif num_menu == 4:
        if not expenses:
            print("❗ Список расходов пуст.\n")
        else:
            print_report(expenses)
            idx_input = input("Введите номер расхода для удаления: ").strip()
            if is_int(idx_input):
                idx = int(idx_input)
                delete_expense(expenses, idx)
            else:
                print("❌ Введите число.\n")

    elif num_menu == 5:
        print("До свидания!")
        break

    else:
        print("❌ Неверный пункт. Повторите ввод.\n")