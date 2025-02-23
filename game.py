import tkinter as tk
from PIL import Image, ImageTk
import pygame

# Ініціалізація Pygame для звуку
pygame.mixer.init()
sound = pygame.mixer.Sound("C:/звягінцев/kliker/hlyist-odin-udar-knuta-26437 (mp3cut.net).mp3")

class ClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Клікер")

        # Лічильник кліків
        self.counter = 0
        self.label = tk.Label(root, text="Кліки: 0", font=("Arial", 14))
        self.label.pack()

        # Завантаження зображення
        image = Image.open("C:/звягінцев/kliker/kiwi.jpg")  # Відкриваємо JPG через Pillow
        self.img = ImageTk.PhotoImage(image)

        # Кнопка з картинкою
        self.button = tk.Button(root, image=self.img, command=self.on_click, borderwidth=0)
        self.button.pack()

    def on_click(self):
        self.counter += 1
        self.label.config(text=f"Кліки: {self.counter}")
        sound.play()

# Запуск програми
root = tk.Tk()
app = ClickerApp(root)
root.mainloop()