import os
from flask import Flask, request, render_template
from keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
from jinja2 import Environment

app = Flask(__name__)
PATH_TO_MODEL = ""
model = load_model(PATH_TO_MODEL)

env = Environment()
env.globals.update(enumerate=enumerate)

class_names = ['ancient_city_(mueang_boran)', 'big_buddha_phuket', 'big_buddha_temple_(wat_phra_yai)', 
               'chaithararam_temple_(wat_chalong)', 'chinatown_-_bangkok', 'historic_city_of_ayutthaya', 
               'jim_thompson_house', 'sukhothai_historical_park', 'temple_of_dawn_(wat_arun)', 'temple_of_the_emerald_buddha_(wat_phra_kaew)', 
               'temple_of_the_golden_buddha_(wat_traimit)', 'the_golden_mount_(wat_saket)', 'the_grand_palace', 'the_sanctuary_of_truth', 
               'tiger_cave_temple_(wat_tham_suea)', 'wat_chedi_luang_varavihara', 'wat_phra_chetuphon_(wat_pho)', 'wat_phra_singh', 'wat_rong_khun', 'wat_umong']

@app.route('/')
def home():
	return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    
    upload_folder = './temp/'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    image_file = request.files['image']
    if not image_file:
        return render_template('index.html', prediction=None)

    # Save the uploaded image to a temporary file
    image_path = os.path.join(upload_folder, image_file.filename)
    image_file.save(image_path)

    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image.astype('float32') / 255.0

    prediction = model.predict(image)[0]
    top_index = np.argmax(prediction)
    top_class = class_names[top_index]
    top_probability = round(prediction[top_index] * 100, 2)

    return render_template('index.html', prediction=(top_class, top_probability))

@app.route('/classes')
def classes():
    strings = class_names
    return render_template('classes.html', strings=strings)


if __name__ == '__main__':
    app.run(debug=True)
