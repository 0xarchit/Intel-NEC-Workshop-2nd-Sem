import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("Calculator")
root.geometry("400x600")
scvl = tkinter.StringVar()
scvl.set("")
screen = tkinter.Entry(root, textvar=scvl, font=("Arial", 30), justify="right")
screen.pack(fill="both", expand=True)

def equal():
    try:
        result = eval(screen.get())
        scvl.set(result)
    except:
        messagebox.showerror("Error", "Invalid Entry")
        scvl.set("")

def clear():
    scvl.set("")

def clear_entry():
    scvl.set("")

button_frame = tkinter.Frame(root)
button_frame.pack(fill="both", expand=True)

button_list = [
    '7',  '8',  '9', '/',
    '4',  '5',  '6', '*',
    '1',  '2',  '3', '-',
    '0',  '.',  '=', '+',
    'C', 'CE'
]

row_val = 0
col_val = 0

for button in button_list:
    tkinter.Button(button_frame, text=button, width=5, command=lambda button=button: click_button(button)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

def click_button(button):
    if button == '=':
        equal()
    elif button == 'C':
        clear()
    elif button == 'CE':
        clear_entry()
    else:
        scvl.set(scvl.get() + str(button))

root.mainloop()

