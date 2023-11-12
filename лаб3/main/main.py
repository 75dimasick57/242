import PySimpleGUI as sg
import my_module

def main():
    """
    Основна функція для виконання графічного інтерфейсу.

    Використовує PySimpleGUI для створення вікна з кнопками та виведенням результатів.
    """
    sg.theme('LightBlue2')

    # Опис графічного інтерфейсу
    layout = [
        [sg.Text("Початковий список чисел:")],
        [sg.Output(size=(30, 10), key='-OUTPUT-')],
        [sg.Button("Перемішати"), sg.Button("Видалити вивід"), sg.ColorChooserButton("Змінити колір")],
        [sg.Text("Кількість елементів:"), sg.Text("", size=(15, 1), key='-COUNT-')],
        [sg.Button("Вийти")]
    ]

    # Створення вікна
    window = sg.Window('Графічна програма', layout)

    while True:
        event, values = window.read()

        # Перевірка подій вікна
        if event in (sg.WINDOW_CLOSED, "Вийти"):
            break
        elif event == "Перемішати":
            my_module.shuffle_and_display(window)
        elif event == "Видалити вивід":
            window['-OUTPUT-'].update('')
            window['-COUNT-'].update('')
        elif event == "Змінити колір":
            color = sg.popup_get_color()
            if color:
                window['-OUTPUT-'].update("Ви вибрали колір: {}".format(color))
        elif event == "Видалити вивід":
            window['-OUTPUT-'].update('')
            window['-COUNT-'].update('')

    # Закриття вікна при завершенні роботи
    window.close()

if __name__ == "__main__":
    main()