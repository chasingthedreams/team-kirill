import tkinter as tk

def click():
    global count
    count += 1
    label.config(text=f"Кликов: {count}")

def reset():
    global count
    count = 0
    label.config(text=f"Кликов: {count}")
