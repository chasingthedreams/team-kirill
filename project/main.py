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
window.resizable(False,False)

count = 0
label = tk.Label(window, text="Кликов: 0", font=("Arial", 20))
label.pack(pady=30)
btn_click = tk.Button(window, text="КЛИК!", command=click, 
          bg="lightblue", font=("Arial", 14)).pack(pady=20)

btn_reset= tk.Button(window, text="Сброс",
                     command = reset, width=10, height=1, font=("Arial", 14))
btn_reset.pack(pady=5)
window.mainloop()
