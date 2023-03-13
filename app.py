from flask import Flask, jsonify

#from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def firstRoute():
    return jsonify({'message': 'Success!!'})
