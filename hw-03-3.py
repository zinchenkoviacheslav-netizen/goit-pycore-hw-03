import re

def phone_number(number):
    result = re.sub(r"[^+0-9]", "", number)

    if result[:3] == "+38":
        return result
    elif result[:3] == "380":
        return "+" + result
    else:
        return "+38" + result


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

final_numbers = [phone_number(number) for number in raw_numbers]

print(f"Ваші номери: {final_numbers}")
