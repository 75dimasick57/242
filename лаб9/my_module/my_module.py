import random

class NumberShuffler:
    def __init__(self, window):
        self.window = window

    def custom_shuffle(self, input_list):
        shuffled_list = input_list.copy()
        random.shuffle(shuffled_list)
        return shuffled_list

    def shuffle_and_display(self):
        numbers = list(range(1, 11))
        shuffled_numbers = self.custom_shuffle(numbers)
        self.window['-OUTPUT-'].update("Початковий список чисел: {}\nПеремішаний список чисел: {}".format(numbers, shuffled_numbers))
        self.window['-COUNT-'].update(len(shuffled_numbers))

class ColorChanger:
    def __init__(self, window):
        self.window = window

    def change_color(self):
        color = sg.popup_get_color()
        if color:
            self.window['-OUTPUT-'].update("Ви вибрали колір: {}".format(color))