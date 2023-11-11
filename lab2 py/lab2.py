import random
import PySimpleGUI as sg

def custom_shuffle(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

def main():
    sg.theme('LightBlue2')  

    layout = [
        [sg.Text("Початковий список чисел:")],
        [sg.Output(size=(30, 10), key='-OUTPUT-')],
        [sg.Button("Перемішати")],
        [sg.Button("Вийти")]
    ]

    window = sg.Window('Графічна програма', layout)

    numbers = list(range(1, 11))

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Вийти"):
            break
        elif event == "Перемішати":
            shuffled_numbers = custom_shuffle(numbers)
            window['-OUTPUT-'].update("Початковий список чисел: {}\nПеремішаний список чисел: {}".format(numbers, shuffled_numbers))

    window.close()

if __name__ == "__main__":
    main()
