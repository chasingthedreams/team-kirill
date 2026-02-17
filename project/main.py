import tkinter as tk

def click():
    global count
    count += 1
    label.config(text=f"Кликов: {count}")

def reset():
    global count
    count = 0
    label.config(text=f"Кликов: {count}")
window = tk.Tk()
window.title("Счетчик кликов")
window.geometry("250x200")

count = 0

# Кнопка для кликов
tk.Button(window, text="Кликни меня!", command=click, 
          bg="lightblue", font=("Arial", 14)).pack(pady=20)
