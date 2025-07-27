import tkinter as tk
import numpy as np

root = tk.Tk()
root.title("Matrix Visual Calculator")

display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = np.array([
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
])

def on_click(char):
    if char == '=':
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, char)

for i in range(buttons.shape[0]):
    for j in range(buttons.shape[1]):
        btn_text = buttons[i, j]
        btn = tk.Button(root, text=btn_text, width=5, height=2, font=("Arial", 18),
                        command=lambda ch=btn_text: on_click(ch))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()
