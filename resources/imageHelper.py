from PIL import Image
from tensorflow.keras.applications.nasnet import preprocess_input
import io
import numpy as np
import base64

labels_list = ['Apple', 'Asparagus', 'Aubergine', 'Avocado', 'Banana', 'Brown-Cap-Mushroom', 'Cabbage', 'Carrots', 'Cucumber', 'Ginger', 'Juice', 'Kiwi', 'Leek', 'Lemon', 'Lime', 'Mango', 'Melon', 'Milk', 'Oat-Milk', 'Oatghurt', 'Onion', 'Orange', 'Passion-Fruit', 'Peach', 'Pear', 'Pepper', 'Pineapple', 'Pomegranate', 'Potato', 'Red-Beet', 'Red-Grapefruit', 'Satsumas', 'Sour-Cream', 'Soyghurt', 'Tomato', 'Yoghurt', 'Zucchini']

def load_img_from_bytes(img_bytes):
    img = Image.open(io.BytesIO(img_bytes.read()))
    img = img.convert('RGB')
    img = img.resize((224, 224), Image.NEAREST)
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    images = np.vstack([img])

    return images

def predict_image(model, img):
    pred = model.predict(img)
    predicted_class_indices = np.argmax(pred, axis = 1)
    labels = [labels_list[i] for i in predicted_class_indices]

    return labels[0]