import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Calculator")
window.iconbitmap("keys.ico")

def bu(num):
    cur = e1.get()
    e1.delete(0, tk.END)
    e1.insert(0, str(cur) + str(num))

def cl():
    e1.delete(0, tk.END)

from tkinter import messagebox

def eq():
    e = e1.get()
    try:
        if "/0" in e.replace(" ", ""):
            messagebox.showerror("Error", "Division by zero is not allowed.")
            return
        cur1 = str(eval(e))
        e1.delete(0, tk.END)
        e1.insert(0, cur1)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except Exception:
        messagebox.showerror("Error", "Invalid expression.")


    e1.delete(0, tk.END)
    e1.insert(0, cur1)
    file=open("history.txt", "a") 
    file.write(e + " = " + cur1 + "\n")
    file.close()

def backspace():
    cur = e1.get()
    e1.delete(0, tk.END)
    e1.insert(0, cur[:-1])

def show_history():
    try:
        file=open("history.txt", "r") 
        data = file.read()
        file.close()
    except:
        data = "No history found."

    hist_win = tk.Toplevel(window)
    hist_win.title("Past Calculations")
    tk.Label(hist_win, text=data, justify="left", font=("Arial", 12)).pack(padx=10, pady=10)

def clear_history():
    open("history.txt", "w").close()
def key_event(event):
    key = event.keysym
    char = event.char

    if key in ['Return', 'KP_Enter']:
        eq()
        return "break"
    elif key == 'BackSpace':
        cur = e1.get()
        e1.delete(0, tk.END)
        e1.insert(0, cur[:-1])
        return "break"
    elif char in '0123456789+-*/().%':
        bu(char)
        return "break"    

e1 = tk.Entry(window, width=18, font=("Arial", 20),bd=2,fg="white",bg="#3e3d3d",insertbackground="white", justify='right')
e1.grid(row=0, column=0, columnspan=5, sticky="nsew")


b1 = tk.Button(window, text="1", padx=30, pady=30, font=("Arial", 12),bg="#0f0f0f",fg='white', command=lambda: bu(1))
b2 = tk.Button(window, text="2", padx=30, pady=30, font=("Arial", 12), bg="#0f0f0f",fg='white',command=lambda: bu(2))
b3 = tk.Button(window, text="3", padx=30, pady=30, font=("Arial", 12), bg="#0f0f0f",fg='white',command=lambda: bu(3))
b4 = tk.Button(window, text="4", padx=30, pady=30, font=("Arial", 12), bg="#0f0f0f",fg='white',command=lambda: bu(4))
b5 = tk.Button(window, text="5", padx=30, pady=30, font=("Arial", 12), bg="#0f0f0f",fg='white',command=lambda: bu(5))
b6 = tk.Button(window, text="6", padx=30, pady=30, font=("Arial", 12),bg="#0f0f0f", fg='white',command=lambda: bu(6))
b7 = tk.Button(window, text="7", padx=30, pady=30, font=("Arial", 12),bg="#0f0f0f", fg='white',command=lambda: bu(7))
b8 = tk.Button(window, text="8", padx=30, pady=30, font=("Arial", 12),bg="#0f0f0f", fg='white',command=lambda: bu(8))
b9 = tk.Button(window, text="9", padx=30, pady=30, font=("Arial", 12),bg="#0f0f0f", fg='white',command=lambda: bu(9))
b0 = tk.Button(window, text="0", padx=30, pady=30, font=("Arial", 12),bg="#0f0f0f", fg='white',command=lambda: bu(0))
bdot = tk.Button(window, text=".", padx=22, pady=20, font=("Arial", 12),bg="#0f0f0f",fg='white', command=lambda: bu("."))

bc = tk.Button(window, text="Clear", padx=10, pady=20, font=("Arial", 12), bg="#202020",fg='white',command=cl)
add = tk.Button(window, text="+", padx=22, pady=20, font=("Arial", 12), bg="#202020",fg='white',command=lambda: bu("+"))
sub = tk.Button(window, text="-", padx=22, pady=20, font=("Arial", 12),bg="#202020",fg='white', command=lambda: bu("-"))
mul = tk.Button(window, text="*", padx=22, pady=20, font=("Arial", 12),bg="#202020", fg='white',command=lambda: bu("*"))
div = tk.Button(window, text="/", padx=22, pady=20, font=("Arial", 12),bg="#202020", fg='white',command=lambda: bu("/"))
equal = tk.Button(window, text="=", padx=20, pady=20, font=("Arial", 12),bg="#0282FB",fg='white', command=eq)
back = tk.Button(window, text="⌫", padx=20, pady=20, font=("Arial", 12),bg="#202020", fg='white',command=backspace)
history = tk.Button(window, text="📜", padx=20, pady=20, font=("Arial", 12),bg="#202020",fg='white', command=show_history)
bclearhis = tk.Button(window, text="🧹", padx=20, pady=20, font=("Arial", 12),bg="#0f0f0f", fg='white',command=clear_history)


b7.grid(row=1, column=0, sticky="nsew")
b8.grid(row=1, column=1, sticky="nsew")
b9.grid(row=1, column=2, sticky="nsew")
add.grid(row=1, column=3, sticky="nsew")

b4.grid(row=2, column=0, sticky="nsew")
b5.grid(row=2, column=1, sticky="nsew")
b6.grid(row=2, column=2, sticky="nsew")
sub.grid(row=2, column=3, sticky="nsew")

b1.grid(row=3, column=0, sticky="nsew")
b2.grid(row=3, column=1, sticky="nsew")
b3.grid(row=3, column=2, sticky="nsew")
mul.grid(row=3, column=3, sticky="nsew")

b0.grid(row=4, column=0, sticky="nsew")
bdot.grid(row=4, column=1, sticky="nsew")
history.grid(row=5, column=2, sticky="nsew")
bclearhis.grid(row=4, column=2, sticky="nsew")
div.grid(row=4, column=3, sticky="nsew")

bc.grid(row=5, column=0, sticky="nsew")
back.grid(row=5, column=1, sticky="nsew")
equal.grid(row=5, column=3, sticky="nsew")


window.bind_all("<Key>", key_event)

window.mainloop()
