import datetime

events = []

'''Призначення:
Виводить привітальне повідомлення, коли користувач запускає програму.
Принцип роботи:
Просто виконує print(...), показуючи користувачу текст:
"Привіт! Я твій органайзер подій. Введи 'допомога' для перегляду команд."'''
def greet():
    print("Привіт! Я твій органайзер подій. Введи 'допомога' для перегляду команд.")

'''Призначення:
Показує список доступних команд, які користувач може вводити.
Принцип роботи:
Використовує print(...), щоб вивести кожну можливу команду.'''
def show_help():
    print("Список команд:")
    print("Додати подію")
    print("Показати події")
    print("Події на тиждень")
    print("Пошук за категорією")
    print("Видалити подію")
    print("Вийти")

'''Призначення:
Дозволяє користувачу додати нову подію в список events.
Принцип роботи:
Просить ввести назву, дату та категорію/опис.
Перетворює дату зі строки у формат datetime.date.
Якщо дата правильна — створює словник з подією та додає його в список events.
Якщо дата введена неправильно — повідомляє про помилку.'''
def add_event():
    name = input("Назва події: ")
    date_str = input("Дата: ")
    category = input("Категорія/опис: ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        events.append({"name": name, "date": date, "category": category})
        print("Подію додано успішно!")
    except ValueError:
        print("Невірний формат дати. Спробуйте ще раз.")

'''Призначення:
Виводить усі збережені події.
Принцип роботи:
Перевіряє, чи список events не порожній.
Якщо є події — виводить кожну у зручному форматі.
Якщо список порожній — повідомляє, що подій немає.'''
def show_events():
    if not events:
        print("Подій не знайдено.")
        return
    print("Список подій:")
    for event in events:
        print(f" Назва: {event['name']}, Дата: {event['date']}, Категорія/Опис: {event['category']}")

'''Призначення:
Показує тільки ті події, які відбуваються на цьому тижні (з понеділка по неділю).
Принцип роботи:
Визначає сьогоднішню дату.
Обчислює початок і кінець поточного тижня.
Фільтрує події з events, які потрапляють у цей діапазон.
Виводить ці події або повідомляє, що їх немає.'''
def events_this_week():
    today = datetime.date.today()
    start_week = today - datetime.timedelta(days=today.weekday())
    end_week = start_week + datetime.timedelta(days=6)
    week_events = [e for e in events if start_week <= e['date'] <= end_week]
    if not week_events:
        print("На цьому тижні немає подій.")
        return
    print("Події на цьому тижні:")
    for event in week_events:
        print(f" Назва: {event['name']}, Дата: {event['date']}, Категорія/Опис: {event['category']}")

'''Призначення:
Дозволяє знайти події за ключовим словом у категорії.
Принцип роботи:
Користувач вводить слово для пошуку.
Програма перетворює його на нижній регістр для порівняння.
Шукає події, у яких це слово є у полі category.
Виводить знайдені події або повідомляє, що нічого не знайдено.'''
def search_by_category():
    keyword = input("Введіть категорію для пошуку: ").lower()
    matches = [e for e in events if keyword in e['category'].lower()]
    if not matches:
        print("Подій за цією категорією не знайдено.")
        return
    print("Знайдені події:")
    for event in matches:
        print(f" Назва: {event['name']}, Дата: {event['date']}, Категорія/Опис: {event['category']}")

'''Призначення:
Видаляє подію зі списку events за її назвою і датою.
Принцип роботи:
Користувач вводить назву події та дату.
Дата перетворюється у формат datetime.date.
Програма перебирає список events і шукає збіг за назвою та датою.
Якщо знаходить — видаляє подію та повідомляє про це.
Якщо не знаходить — виводить повідомлення.
Якщо дата введена неправильно — повідомляє про помилку.'''
def delete_event():
    name = input("Назва події для видалення: ")
    date_str = input("Дата події: ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        for e in events:
            if e['name'].lower() == name.lower() and e['date'] == date:
                events.remove(e)
                print("Подію видалено.")
                return
        print("Подію не знайдено.")
    except ValueError:
        print("Невірний формат дати.")

'''Призначення:
Основна функція, яка керує взаємодією з користувачем і викликає інші функції.
Принцип роботи:
Виводить привітання (greet()).
Запускає нескінченний цикл while True.
Чекає введення команди.
Порівнює введення з доступними командами.
Якщо команда відома — викликає відповідну функцію.
Якщо "вийти" — завершує програму.
Якщо команда невідома — виводить повідомлення-підказку.'''
def main():
    greet()
    while True:
        command = input("Введіть команду: ").strip().lower()
        if command == "допомога":
            show_help()
        elif command == "додати подію":
            add_event()
        elif command == "показати події":
            show_events()
        elif command == "події на тиждень":
            events_this_week()
        elif command == "пошук за категорією":
            search_by_category()
        elif command == "видалити подію":
            delete_event()
        elif command == "вийти":
            print("До побачення!")
            break
        else:
            print("Невідома команда. Введіть 'допомога' для списку доступних команд.")
            
'''Призначення:
Забезпечує запуск функції main() тільки тоді, коли файл запускається напряму, а не імпортується в інший.
Принцип роботи:
Перевіряє, чи файл виконується як головний.
Якщо так — запускає main().'''
if __name__ == "__main__":
    main()
