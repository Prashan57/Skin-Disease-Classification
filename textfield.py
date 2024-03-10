import tkinter as tk

def on_button_click():
    entered_text = entry.get()
    result_label.config(text=f"You entered: {entered_text}")

# Create the main window
root = tk.Tk()
root.title("Tkinter Text Field Example")

# Create a text field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to capture the text field value
button = tk.Button(root, text="Get Value", command=on_button_click)
button.pack(pady=10)

# Display the captured value
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
