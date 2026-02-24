import random

def get_numbers_ticket(min_v, max_v, quantity):

    if not (1 <= min_v <= 1000):
        return []
    if not (1 <= max_v <= 1000):
        return []
    if min_v > max_v:
        return []
    if not (1 <= quantity <= (max_v - min_v + 1)):
        return []

    return sorted(random.sample(range(min_v, max_v + 1), quantity))

while True:
    try:
        min_v, max_v, quantity_v = map(int, input("Введіть min max quantity: ").split())
        break
    except ValueError:
        print("Некоректні данні, спробуй ще раз")

print(get_numbers_ticket(min_v, max_v, quantity_v))
