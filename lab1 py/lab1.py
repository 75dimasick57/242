import random  # Імпортуємо модуль random

def main():
    # Головна функція програми
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffled_numbers = custom_shuffle(numbers)
    print("Початковий список чисел:", numbers)
    print("Перемішаний список чисел:", shuffled_numbers)

def custom_shuffle(input_list):
    # Функція для перемішування списку чисел
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

if __name__ == "__main__":
    main()  # Викликаємо головну функцію, якщо програма запущена як скрипт
