import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Uploader")

        self.image_label = tk.Label(root, text="No Image Selected", font=("Arial", 12))
        self.image_label.pack(pady=20)

        self.path_label = tk.Label(root, text="", font=("Arial", 10), wraplength=400)
        self.path_label.pack(pady=10)

        browse_button = tk.Button(root, text="Browse", command=self.browse_image, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        browse_button.pack(pady=20)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            image = Image.open(file_path)
            image.thumbnail((400, 400))  # Resize image if needed
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(text="")
            self.image_label.configure(image=photo)
            self.image_label.image = photo

            self.path_label.config(text=f"Image Path: {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x700")
    root.configure(bg="#f0f0f0")  # Set background color

    app = ImageUploaderApp(root)
    root.mainloop()
