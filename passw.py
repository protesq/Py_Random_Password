import random
import string
import tkinter as tk
from tkinter import messagebox

def home():
    global pass_entry
    home_page = tk.Tk()
    home_page.title("Anasayfa")
    screen_width = home_page.winfo_screenwidth()
    screen_height = home_page.winfo_screenheight()

    window_height = 600
    window_width = 700

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    home_page.geometry(f"{window_width}x{window_height}+{x}+{y}")
    home_page.config(bg="white")

    pass_entry = tk.Entry(home_page, width=40)
    pass_entry.pack(pady=20)

    pass_button = tk.Button(home_page, text="Şifreyi Oluştur", command=generate_pass)
    pass_button.pack()

    home_page.mainloop()

def generate_pass(length=12):
    pass_get = pass_entry.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(random.choice(characters) for _ in range(length))
    messagebox.showinfo("Uyarı !", f"Şifre : {passw}")

if __name__ == "__main__":
    home()

