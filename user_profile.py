import tkinter as tk
#В этом проекте profile_image.png имеет прозрачные части, но tkinter сам по себе не работате с ними, подключаем PIL чтобы поменять фон
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        "Настройки графического интерфейса приложения."
        self.geometry("250x400+50+50")
        self.title("2.1 - User Profile GUI")

        self.setUpMainWindow()

    def createImageLabels(self):
        "Открывает файлы изображений и создаёт метки изображений."
        #Label не работает с прозрачными частями, поэтому подключаем canvas
        self.canvas = tk.Canvas(self)
        self.canvas.place(width=250, height=400)
        images = ["images/skyblue.png", "images/profile_image.png"]
        for image in images:
            try:
                with open(image):
                    img = Image.open(image)
                    photo = ImageTk.PhotoImage(img)

                    if image == "images/profile_image.png":
                        self.canvas.place(x=0, y=0)
                        self.canvas.create_image( 80, 20,image=photo, anchor='nw')
                        setattr(self, f"photo_{image.replace('/', '_')}", photo)  # сохраняем ссылку
                    else:
                        self.canvas.create_image(0, 0, image=photo, anchor='nw')
                        setattr(self, f"photo_{image.replace('/', '_')}", photo)

            except FileNotFoundError as error:
                print(f"Images not found. \nError: {error}")

    def setUpMainWindow(self):
        """Создаём метки, которые будут отображаться в окне."""
        self.createImageLabels()
        user_label = tk.Label(self, text="Иван Драго", font=("Arial", 20))
        user_label.place(x=55, y=140)

        bio_label = tk.Label(self, text="Биография", font=("Arial", 17))
        bio_label.place(x=15, y=170)

        about_label = tk.Label(self, text="Я инженер-прогрммист с 10-летнем\
                                        опытом создания портрясающего кода", wraplength=220)
        about_label.place(x=15, y=200)

        skills_label = tk.Label(self, text="Умения", font=("Arial", 17))
        skills_label.place(x=15, y=240)

        language_label = tk.Label(self, text="Python | PHP | SQL | JavaScript")
        language_label.place(x=15, y=270)

        experience_label = tk.Label(self, text="Опыт", font=("Arial", 17))
        experience_label.place(x=15, y=290)

        developer_label = tk.Label(self, text="Python Разработчик")
        developer_label.place(x=15, y=320)

        dates_label = tk.Label(self, text="Март 2011 - настоящее время", font=("Arial", 8))
        dates_label.place(x=15, y=340)

        driver_label = tk.Label(self, text="Водитель доставки пиццы")
        driver_label.place(x=15, y=360)

        driver_dates_label = tk.Label(self, text="Aug 2015 - Dec 2017", font=("Arial", 8))
        driver_dates_label.place(x=15, y=380)

# Run program
if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()