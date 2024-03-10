from tensorflow.keras.models import load_model

# Load the saved model
model = load_model('D:\\sem7\\project\\modelTrain1.h5')


from tensorflow.keras.preprocessing import image
import numpy as np


def preprocess_input_image(image_path):
    img = image.load_img(image_path, target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array 	
    
    
    
    # image_path = 'D:\\sem7\\project\\img\\Datasets\\test\\NORMAL\\NORMAL2-IM-0380-0001.jpeg'
image_path = 'D:\\sem7\\project\\img\\Datasets\\test\\PNEUMONIA\\person11_virus_38.jpeg'

input_image = preprocess_input_image(image_path)
predictions = model.predict(input_image)


predicted_class_index = np.argmax(predictions)
print(f'index: {predicted_class_index}')


class_labels = ['Not Pneumonia', 'Pneumonia'] 
predicted_class_label = class_labels[predicted_class_index]


print(f'Predicted Class: {predicted_class_label}')

# print(f'Predicted value is: {predicted_class_index}')