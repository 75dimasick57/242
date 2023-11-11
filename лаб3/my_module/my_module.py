import random

def custom_shuffle(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

def shuffle_and_display(window):
    numbers = list(range(1, 11))
    shuffled_numbers = custom_shuffle(numbers)
    window['-OUTPUT-'].update("Початковий список чисел: {}\nПеремішаний список чисел: {}".format(numbers, shuffled_numbers))