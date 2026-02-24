from datetime import datetime

def get_days_from_today(yourdate: str) -> int:
    your_date = datetime.strptime(yourdate, "%Y-%m-%d").date()
    today = datetime.today().date()
    return (today - your_date).days


while True:
    date_str = input("Введіть дату у форматі YYYY-MM-DD: ").strip()
    try:
        diff_days = get_days_from_today(date_str)
        break
    except ValueError:
        print("Некоректний ввід. Приклад: 2020-10-09")

print(f"Різниця — {diff_days} діб")
