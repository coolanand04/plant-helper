from flask import Flask, render_template, jsonify, request, Markup, make_response, send_from_directory
from model import predict_image
import utils

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)
            print(prediction)
            res = Markup(utils.disease_dic[prediction])
            return render_template('display.html', status=200, result=res)
        except:
            pass
    return render_template('index.html', status=500, res="Internal Server Error")

@app.route("/manifest.json", methods=['GET'])
def manifest():
    return("manifest.json", 200, {'Content-Type': 'application/json'})

@app.route("/sw.js", methods=['GET'])
def sw():
    response=make_response(
                     send_from_directory('sw.js',path='sw.js', as_attachment=True))
    #change the content header file. Can also omit; flask will handle correctly.
    response.headers['Content-Type'] = 'application/javascript'

@app.route("/favicon.ico", methods=['GET'])
def favico():
    return("./static/icons/favicon-310x310.ico", 200, {'Content-Type': 'image/x-icon'})

@app.route("/apple-touch-icon.png", methods=['GET'])
def appleico():
    return("./static/icons/icon-512x512.png", 200, {'Content-Type': 'image/png'})

if __name__ == "__main__":
    app.run(debug=True)
