from tkinter import *
from tkinter import messagebox

def save_text():
    filename = entry.get()
    if filename == "": 
        messagebox.showinfo("Внимание!", "Введите название заметки")
    else:
        with open((filename + '.txt'), "w") as file:
            file.write(text_area.get(1.0, END))
        messagebox.showinfo("Успешно!", "Текст заметки сохранен.")

def open_text():
    filename = entry.get()
    if filename == "":
        messagebox.showinfo("Внимание!", "Введите название заметки")
    else:
        with open((filename + '.txt'), "r") as file:
            text_area.delete(1.0, END) 
            text_area.insert(1.0, file.read())
        messagebox.showinfo("Успешно!", "Заметка открыта")

# GUI
window = Tk()
window.title("Заметки") # GeekBrains
window.geometry("650x450")

label = Label(window, text="Введите название заметки:")
label.grid(row=0, column=0)
entry = Entry(window)
entry.grid(row=0, column=1)

text_area = Text(window)
text_area.grid(row=1, column=0, columnspan=2)

save_btn = Button(window, text="Сохранить заметку", command=save_text) 
save_btn.grid(row=2, column=0)
open_btn = Button(window, text="Открыть заметку", command=open_text) 
open_btn.grid(row=2, column=1)

window.mainloop()