import random

def custom_shuffle(input_list):
    """
    Перемішує вхідний список та повертає новий перемішаний список.

    Args:
        input_list (list): Вхідний список чисел.

    Returns:
        list: Перемішаний список чисел.
    """
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

def shuffle_and_display(window):
    """
    Викликає функцію перемішування та відображення результатів у графічному вікні.

    Args:
        window (PySimpleGUI.Window): Графічне вікно PySimpleGUI.
    """
    numbers = list(range(1, 11))
    shuffled_numbers = custom_shuffle(numbers)
    window['-OUTPUT-'].update("Початковий список чисел: {}\nПеремішаний список чисел: {}".format(numbers, shuffled_numbers))
    window['-COUNT-'].update(len(shuffled_numbers))