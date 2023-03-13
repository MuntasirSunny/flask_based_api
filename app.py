import os

from flask import Flask, jsonify, request
from passporteye import read_mrz

app = Flask(__name__)
import pytesseract
from flask_cors import CORS

#from flask import request


app = Flask(__name__)
CORS(app)
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

@app.route('/', methods=['GET', 'POST'])
def firstRoute():
    return jsonify({'message': 'Success!!'})


@app.route('/process_mrz', methods=['POST'])
def process_mrz():
    # Check if image file was submitted
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})
# Save image file to folder
    image_file = request.files['image']
    image_path = os.path.join("uploads/", image_file.filename)
    print(image_path)
    image_file.save(image_path)
    
    # Read image file and extract MRZ data
    mrz = read_mrz(image_path)
    mrz_data = mrz.to_dict()
    print("MRZ : ", mrz_data)
    # Return MRZ data in JSON format
    return jsonify({
        'country': mrz_data['country'],
        'names': mrz_data['names'],
        'surname': mrz_data['surname'],
        'type': mrz_data['type'],
        'date_of_birth': mrz_data['date_of_birth'],
        'expiration_date': mrz_data['expiration_date'],
        'sex': mrz_data['sex']
    })
