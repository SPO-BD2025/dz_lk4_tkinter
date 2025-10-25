import tkinter as tk


class MainWindow(tk.Tk):                                    #QWidget → Tk
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        'Настройте графический интерфейс приложения.'
        self.geometry("250x250+100+100")                    #setGeometry(100, 100, 250, 250) → geometry("250x250+100+100")
        self.title("Пример Tkinker")                        #setWindowTitle() → title()

        self.setUpMainWindow()
                                                            #Удаляем self.show()
    def setUpMainWindow(self):
        "Создаем Tkinker для отображения в главном окне"
        hello_label = tk.Label(self, text="Привет!")        #QLabel → Label
                                                            #setText() → параметр text=
        hello_label.place(x=105, y=15)                      #move() → place()
        image = "images/world.png"
        try:
            with open(image):
                world_label = tk.Label(self)
                photo = tk.PhotoImage(file=image)           #QPixmap → PhotoImage
                world_label.config(image=photo)
                world_label.image = photo
                world_label.place(x=25, y=40)               #move() → place()

        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")

if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()                                       #QApplication и app.exec() → mainloop()