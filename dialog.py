import tkinter as tk
from tkinter import simpledialog

class CustomDialog(tk.simpledialog.Dialog):
    def dialogBox(self, master):
        tk.Label(master, text="Admin Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        tk.Label(master, text="Admin Password:").grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entry_text1 = tk.Entry(master)
        self.entry_text2 = tk.Entry(master)

        self.entry_text1.grid(row=0, column=1, padx=10, pady=5)
        self.entry_text2.grid(row=1, column=1, padx=10, pady=5)

        return self.entry_text1  # Initial focus on the first entry

    def apply(self):
        admin_name = self.entry_text1.get()
        admin_password = self.entry_text2.get()

        # Do something with the entered text, for example, print it
        print("Entered text 1:", admin_name)
        print("Entered text 2:", admin_password)

# Create the main window
root = tk.Tk()
root.title("Tkinter Two Text Fields Dialog Example")

# Create a button to trigger the custom dialog
button = tk.Button(root, text="Open Two Text Fields Dialog", command=lambda: CustomDialog(root))
button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
