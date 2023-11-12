import PySimpleGUI as sg
from my_module import NumberShuffler, ColorChanger

class GUIApp:
    def __init__(self):
        sg.theme('LightBlue2')
        self.window = sg.Window('Графічна програма', self.get_layout())
        self.number_shuffler = NumberShuffler(self.window)
        self.color_changer = ColorChanger(self.window)

    def get_layout(self):
        return [
            [sg.Text("Початковий список чисел:")],
            [sg.Output(size=(30, 10), key='-OUTPUT-')],
            [sg.Button("Перемішати"), sg.Button("Видалити вивід"), sg.Button("Змінити колір")],
            [sg.Text("Кількість елементів:"), sg.Text("", size=(15, 1), key='-COUNT-')],
            [sg.Button("Вийти")]
        ]

    def run(self):
        while True:
            event, values = self.window.read()

            if event in (sg.WINDOW_CLOSED, "Вийти"):
                break
            elif event == "Перемішати":
                self.number_shuffler.shuffle_and_display()
            elif event == "Видалити вивід":
                self.window['-OUTPUT-'].update('')
                self.window['-COUNT-'].update('')
            elif event == "Змінити колір":
                self.color_changer.change_color()

        self.window.close()

if __name__ == "__main__":
    app = GUIApp()
    app.run()