import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
import tensorflow.compat
import os

class DiseaseClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Uploader")

        self.image_label = tk.Label(root, text="SKIN DISEASE CLASSIFICATION", font=("Arial", 24),bg="#FFF")
        self.image_label.pack(pady=150)
        
        self.image_label = tk.Label(root, text="No Image Selected", font=("Arial", 12),bg="#FFF",fg='grey')
        self.image_label.pack(pady=5)

        self.path_label = tk.Label(root, text="", font=("Arial", 10), wraplength=400 ,bg="#FFF")
        self.path_label.pack(pady=5)

        browse_button = tk.Button(root, text="Browse", command=self.browse_image, font=("Arial", 12), bg="#5a76d1", fg="white", padx=40, pady=10)
        browse_button.pack(pady=5)
        
    def image_declaration(self,image_path):
        # Load the trained model
        model = load_model('/home/prashan/Desktop/defen/gautam.h5')
        new_image_path  = str(image_path)
        print("new",new_image_path)
        # Function to load and preprocess the image
        def load_image(img_path):
            img = Image.open(img_path)
            img = img.resize((100, 75))  # Adjust dimensions to match the model's input shape
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            img /= 255.0  # Normalization
            return img
            
        # Load and preprocess the new image
        # new_image_path = '/home/prashan/Desktop/defen/wart.jpeg'
        
        # new_image_path = string_image_path
        new_image = load_image(image_path)
        print("Line 46 new image",new_image)
        # Make predictions
        
        prediction = model.predict(new_image)
        rounded_prediction = [np.round(value, 2) for value in prediction]
        
        print(rounded_prediction)

        # Assuming you have a list of class names
        classes = [
            'Eczema',
            'Melanoma',
            'Atopic Dermatitis',
            'Basal Cell Carcinoma',
            'Melanocytic Nevi',
            'Benign Keratosis',
            'Psoriasis',
            'Seborrheic Keratoses',
            'Tinea Ringworm Candidiasis',
            'Warts Molluscum and other Viral Infections'
        ]

        # Get the predicted class index
        
        predicted_class_index = np.argmax(prediction)

        # Get the predicted class label
        predicted_class = classes[predicted_class_index]
                
        return predicted_class

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            print("HELLO PATH", file_path)
            disease = self.image_declaration(file_path)
            print("returned", disease)
            image = Image.open(file_path)
            image.thumbnail((400, 400))  # Resize image if needed
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(text="")
            self.image_label.configure(image=photo)
            self.image_label.image = photo

            self.path_label.config(text=f"Image Path: {file_path}")
            self.path_label.config(text=f"Disease Name : {disease}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x900")
    root.configure(bg="#FFF")  # Set background color

    app = DiseaseClassifierApp(root)
    root.mainloop()
