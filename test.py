from keras.models import load_model
import tensorflow.compat.v2 as tf

# Load the saved model
model = load_model('/home/prashan/Desktop/defen/gautam.h5')


from keras.preprocessing import image
import numpy as np


def preprocess_input_image(image_path):
    img = image.load_img(image_path, target_size=(100,75))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array 	
    
image_path = '/home/prashan/Desktop/defen/benzema.jpeg'

input_image = preprocess_input_image(image_path)
predictions = model.predict(input_image)


predicted_class_index = np.argmax(predictions)
print(f'index: {predicted_class_index}')


class_labels = [
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
predicted_class_label = class_labels[predicted_class_index]


print(f'Predicted Class: {predicted_class_label}')

# print(f'Predicted value is: {predicted_class_index}')