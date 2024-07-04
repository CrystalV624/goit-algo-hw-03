# Перше завдання
from datetime import datetime
def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'")
    today = datetime.strptime('2021-05-05', '%Y-%m-%d').date()
    delta = input_date - today
    return delta.days
print(get_days_from_today('2021-10-09'))

# Друге завдання
import random
def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000):
        return []
    if not (1 <= quantity <= (max - min + 1)):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

# Третє завдання
import re
def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    # Якщо номер не починається з '+', додаємо код країни '+38'
    if not phone_number.startswith('+'):
        if phone_number.startswith('380'):
            phone_number = '+' + phone_number
        else:
            phone_number = '+38' + phone_number
    
    return phone_number
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
