import sys

books = {"Сияние": "Стивен Кинг",
         "Зелёная миля": "Стивен Кинг",
         "Мистер Мерседес": "Стивен Кинг",
         "Бегущий человек": "Стивен Кинг",
         "Три мушкетёра": "Александр Дюма",
         "Граф Монте-Кристо": "Александр Дюма",
         "Королева Марго": "Александр Дюма",}

# Проверка наличия аргументов
if len(sys.argv) < 2:
    print("Использование:")
    print("  python script.py filter <автор>")
    print("  python script.py sort <поле>")
    sys.exit(1)

action = sys.argv[1]

if action == "filter":
    if len(sys.argv) < 3:
        print("Для filter нужно указать автора, например: python script.py filter 'Стивен Кинг'")
        sys.exit(1)
    author = sys.argv[2]
    # Отфильтровать книги по автору
    filtered_books = list(filter(lambda title: books[title] == author, books.keys()))
    # Преобразовать в строки "Книга — Автор"
    result = list(map(lambda title: f"{title} — {books[title]}", filtered_books))
    print("Книги автора", author + ":")
    for line in result:
        print("  -", line)

elif action == "sort":
    sort_field = sys.argv[2] if len(sys.argv) > 2 else "book"  # по умолчанию — по названию
    # Подготовим список строк "Книга — Автор"
    books_list = list(map(lambda title: f"{title} — {books[title]}", books.keys()))
    # Сортировка: если sort_field == "author", сортируем по автору (вторая часть после " — ")
    if sort_field == "author":
        books_list.sort(key=lambda s: s.split(" — ")[1])
    else:  # по умолчанию или если "book"
        books_list.sort(key=lambda s: s.split(" — ")[0])
    print("Отсортированный список книг (по", sort_field + "):")
    for line in books_list:
        print("  -", line)

else:
    print(f"Неизвестное действие: {action}")
    print("Доступные: filter, sort")