from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            weekday = birthday_this_year.weekday()

            if weekday == 5:
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif weekday == 6:
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

list_users = [
    {"name": "Олександр Коваль", "birthday": "1990.02.15"},
    {"name": "Марія Шевченко", "birthday": "1985.02.25"},
    {"name": "Маррина Іванко", "birthday": "1985.02.28"},
    {"name": "Андрій Рижов", "birthday": "1985.02.27"},
    {"name": "Володя Пакиш", "birthday": "1985.02.26"},
]

result = get_upcoming_birthdays(list_users)
print(result)

