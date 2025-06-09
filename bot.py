import datetime

events = []

def greet():
    print("Привіт! Я твій органайзер подій. Введи 'допомога' для перегляду команд.")

def show_help():
    print("Список команд:")
    print("Додати подію")
    print("Показати події")
    print("Події на тиждень")
    print("Пошук за категорією")
    print("Видалити подію")
    print("Вийти")
    
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
        
def show_events():
    if not events:
        print("Подій не знайдено.")
        return
    print("Список подій:")
    for event in events:
        print(f"- {event['name']} ({event['date']}) — {event['category']}")
        
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
        print(f"- {event['name']} ({event['date']}) — {event['category']}")
        
def search_by_category():
    keyword = input("Введіть категорію для пошуку: ").lower()
    matches = [e for e in events if keyword in e['category'].lower()]
    if not matches:
        print("Подій за цією категорією не знайдено.")
        return
    print("Знайдені події:")
    for event in matches:
        print(f"- {event['name']} ({event['date']}) — {event['category']}")
        
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

if __name__ == "__main__":
    main()
