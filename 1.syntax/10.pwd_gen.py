# password_google

# импортирование модулей
import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar

def generator():
    # 1. чтение данных строки сырой пароли
    pwd_str = pwd.get()
    # кодирование в байт-строка
    byte_str = pwd_str.encod0
    hash_str = hashlib.sha256(byte_str)
    # преобразование хеш-строки в обычную строку
    hex_str = hash_str.hexdigest()[:10]

    # вывод хеш-строки
    # print(hex_str)
    hash_pwd.set(hex_str)

# generator("qwerty")

# объект окна
window = Tk()
window.title("Pwd generator v.0.1")

# объекты для хранения строк
pwd = StringVar()
hash_pwd = StringVar()

# тестирование stringVar
# pwd.set("qwerty")
# print(pwd.get())

# виджет (компоненты) текстовой метки
lbl = Label(text="Пароль:")
lbl.grid(row=0, column=0)

# виджет поля ввода
Entry(textvariable=pwd).grid(row=0, column=1)

# виджет кнопки
Button(text="СТАРТ", command=generator).grid(row=1, column=0)

# виджет вывода
Entry(textvariable=hash_pwd).grid(row=1, column=1)

# точка входа программы (место, где программа запускается)
window.mainloop()