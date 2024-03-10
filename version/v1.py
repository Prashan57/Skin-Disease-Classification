from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
import tensorflow.compat
# import matplotlib.pyplot as plt
import os

# Load the trained model
model = load_model('/home/prashan/Desktop/defen/gautam.h5')

# Function to load and preprocess the image
def load_image(img_path):
    img = Image.open(img_path)
    img = img.resize((100, 75))  # Adjust dimensions to match the model's input shape
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0  # Normalization
    return img

# Load and preprocess the new image
new_image_path = '/home/prashan/Desktop/defen/wart.jpeg'
new_image = load_image(new_image_path)

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

# # Display the input image
# img = Image.open(new_image_path)
# plt.imshow(img)
# plt.show()

# Print the predicted class
print(f"The disease in the image is classified as: {predicted_class}")
