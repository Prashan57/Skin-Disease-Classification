import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
import tensorflow.compat
import os

import requests
import json

class DiseaseClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Uploader")

        self.image_label = tk.Label(root, text="SKIN DISEASE CLASSIFICATION", font=("Arial", 24),bg="#FFF")
        self.image_label.pack(pady=100)
        
        self.image_label = tk.Label(root, text="Write Doctor Name And Select Image", font=("Arial", 12),bg="#FFF",fg='grey')
        self.image_label.pack(pady=5)
        
        # Create a text field
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        self.path_label = tk.Label(root, text="", font=("Arial", 11) ,wraplength="400",bg="#FFF")
        self.path_label.pack(pady=5)

        browse_button = tk.Button(root, text="Browse", command=self.browse_image, font=("Arial", 12), bg="#5a76d1", fg="white", padx=40, pady=10)
        browse_button.pack(pady=5)
        
        
        # browse_button = tk.Button(root, text="Save to DB", command=self.disease_data_storeDB, font=("Arial", 12), bg="#5a76d0", fg="white", padx=40, pady=10)
        # browse_button.pack(pady=10)
        
        self.disease_info = {
            'Eczema': {
                'Description': 'Eczema is a common skin condition characterized by red, itchy, and inflamed skin. It often occurs in patches and can be chronic.',
                'Treatment': 'Treatment may include moisturizers, topical steroids, antihistamines, and avoiding triggers.'
            },
            'Melanoma': {
                'Description': 'Melanoma is a type of skin cancer that develops from pigment-containing cells known as melanocytes. It is often characterized by the appearance of moles with irregular borders and colors.',
                'Treatment': 'Treatment typically involves surgical removal of the melanoma. In advanced cases, additional therapies such as immunotherapy or targeted therapy may be considered.'
            },
            'Atopic Dermatitis': {
                'Description': 'Atopic dermatitis, or eczema, is a chronic skin condition that results in itchy, inflamed skin. It is common in individuals with a personal or family history of allergic conditions.',
                'Treatment': 'Management involves moisturizers, topical steroids, antihistamines, and identifying and avoiding triggers.'
            },
            'Basal Cell Carcinoma': {
                'Description': 'Basal cell carcinoma is a type of skin cancer that originates in the basal cells of the skin. It is the most common type of skin cancer and usually appears as a shiny or pearly bump.',
                'Treatment': 'Treatment often involves surgical removal of the affected area. In some cases, other therapies such as cryotherapy or topical medications may be considered.'
            },
            'Melanocytic Nevi': {
                'Description': 'Melanocytic nevi, commonly known as moles, are benign growths on the skin. They are usually brown or black and can vary in size and shape.',
                'Treatment': 'Most melanocytic nevi do not require treatment. If a mole changes in size, shape, or color, or if there are concerns about it, medical evaluation is recommended.'
            },
            'Benign Keratosis': {
                'Description': 'Benign keratosis refers to non-cancerous skin lesions that often appear as raised, scaly, or wart-like growths.',
                'Treatment': 'Treatment may involve removal if the lesion causes discomfort or for cosmetic reasons. Options include cryotherapy, laser therapy, or surgical excision.'
            },
            'Psoriasis': {
                'Description': 'Psoriasis is a chronic autoimmune condition that results in the rapid buildup of skin cells, leading to the formation of thick, scaly patches. It can affect various parts of the body.',
                'Treatment': 'Treatment options include topical medications, phototherapy, oral medications, and biologic drugs. The choice of treatment depends on the severity and location of psoriasis.'
            },
            'Seborrheic Keratoses': {
                'Description': 'Seborrheic keratoses are non-cancerous skin tumors that appear as wart-like growths. They are common in older individuals and may vary in color from tan to black.',
                'Treatment': 'Seborrheic keratoses are usually benign and do not require treatment. If removal is desired for cosmetic reasons, options include cryotherapy, laser therapy, or surgical excision.'
            },
            'Tinea Ringworm Candidiasis': {
                'Description': 'Tinea refers to a group of fungal infections that can affect the skin, hair, or nails. Ringworm and candidiasis are examples of tinea infections.',
                'Treatment': 'Antifungal medications, both topical and oral, are commonly used to treat tinea infections. Keeping the affected area clean and dry is also important for management.'
            },
            'Warts Molluscum and other Viral Infections': {
                'Description': 'Warts, molluscum contagiosum, and other viral infections are caused by various viruses. They can result in the formation of skin growths or lesions.',
                'Treatment': 'Treatment options vary and may include topical treatments, cryotherapy, laser therapy, or other procedures depending on the specific viral infection.'
            }
        }

        
    def login(self):
        print("Login")
        apiEndpoint = "http://localhost:4000/api/read"
        response = requests.get(apiEndpoint)
        print(response.json())
        
    # def disease_data_storeDB(self,file_path,disease_name):
    #     print("History Data Store in DB",predicted_class)
    #     apiEndpoint = "http://localhost:4000/history"
    #     response = requests.post(apiEndpoint, data = {'name': 'User', 'filePath': file_path , 'disease': disease_name})
    #     print(response.json())
    
    
    def image_declaration(self,image_path,doctor_name):
        # Load the trained model
        print("Doctor Name from image ---------",doctor_name)
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
        print("Line 46 new image &&& DOCCC",new_image , doctor_name)
        # Make predictions
        
        prediction = model.predict(new_image)
        
        
        
        rounded_prediction = [np.round(value, 2) for value in prediction]
        
        print('hello',rounded_prediction)
        
        #filter out the values less than 0.5 and store them in a variable
        # filtered_prediction = [value for value in prediction if value > 0.5]
        # print('filtered_prediction',filtered_prediction)
                
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
        global predicted_class 
        
        predicted_class= classes[predicted_class_index]
        
        # def disease_data_storeDB(self,file_path,disease_name):
        print("History Data Store in DB",predicted_class)
        apiEndpoint = "http://localhost:4000/history"
        response = requests.post(apiEndpoint, json = {"name":doctor_name,"filePath":new_image_path,"disease":predicted_class})
        print(response.json())
        
        # self.disease_data_storeDB(new_image_path,predicted_class)
                
        return predicted_class

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            print("HELLO PATH", file_path)
            doctor_name = self.entry.get()
            print("Doctor Name -------- ",doctor_name)
            disease = self.image_declaration(file_path,doctor_name)
            print("returned", disease)
            image = Image.open(file_path)
            image.thumbnail((400, 400))  # Resize image if needed
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(text="")
            self.image_label.configure(image=photo)
            self.image_label.image = photo
           
            # arr = self.disease_info
            # print("Mggg",arr)       
            global description,treatment
            if disease in self.disease_info:
                print("Disease information found",disease)
                string_disease = str(disease)
                description = self.disease_info[string_disease]['Description']
                print("Description",description)
                treatment = self.disease_info[string_disease]['Treatment']
                print("Treatment",treatment)
                self.path_label.config(text=f"Disease Name : {disease}\n\nDescription: {description}\n\nTreatment: {treatment}")
            else:
                print("Disease information not found")
                
            # self.path_label.config(text=f"Image Path: {file_path}")
            self.path_label.config(text=f"Disease Name : {disease}\n\nDescription : {description}\n\nTreatment : {treatment}\n\nDiagnostician Name : {doctor_name}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x900")
    root.configure(bg="#FFF")  # Set background color

    app = DiseaseClassifierApp(root)
    root.mainloop()
