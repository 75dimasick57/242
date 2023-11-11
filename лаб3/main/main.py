import PySimpleGUI as sg
import my_module

def main():
    sg.theme('LightBlue2')

    layout = [
        [sg.Text("Початковий список чисел:")],
        [sg.Output(size=(30, 10), key='-OUTPUT-')],
        [sg.Button("Перемішати"), sg.ColorChooserButton("Змінити колір")],
        [sg.Button("Вийти")]
    ]

    window = sg.Window('Графічна програма', layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Вийти"):
            break
        elif event == "Перемішати":
            my_module.shuffle_and_display(window)
        elif event == "Змінити колір":
            color = sg.popup_get_color()
            window['-OUTPUT-'].update("Ви вибрали колір: {}".format(color))

    window.close()

if __name__ == "__main__":
    main()