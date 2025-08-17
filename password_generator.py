import tkinter as tk
import random, string

def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    root.clipboard_clear()
    root.clipboard_append(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

tk.Label(root, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate", command=generate_password)
generate_btn.pack(pady=10)

result_entry = tk.Entry(root, width=40)
result_entry.pack(pady=5)

root.mainloop()
