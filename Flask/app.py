from flask import Flask, render_template, request, jsonify
from markupsafe import Markup
from model import predict_image
import utils

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            res = Markup(utils.disease_dic.get(prediction, 'Unknown disease'))
            return render_template('display.html', result=res)
        except Exception as e:
            print(e)
            return render_template('index.html', status=500, res="Internal Server Error")
    return render_template('index.html', status=500, res="Internal Server Error")

if __name__ == "__main__":
    app.run(debug=True)
