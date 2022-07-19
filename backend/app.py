from flask import Flask
from flask_cors import CORS
import calc
import ml

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
def hello_world():
    return "<p>Hello, <b>World!</b></p>"

@app.route("/showcolor")
def show_color():
    return "<p style='color:blue;background-color:yellow'>This is a text with color</p>"

@app.route("/prediction/<algo>")
def prediction(algo):
    # n1 = escape(n1)
    # a = calc.add(int(n1), int(n2))
    pred = str(ml.predict(algo))
    return "Algorithm= " + algo + "<br /> Prediction: " + pred
 #   return "<h1>" + str(a) + "</h1>" 

@app.route("/add/<n1>-and-<n2>")
def add_numbers(n1, n2):
    # n1 = escape(n1)
    a = calc.add(int(n1), int(n2))
    return "<h1>" + str(a) + "</h1>" 

if __name__ == "__main__":
    app.run()