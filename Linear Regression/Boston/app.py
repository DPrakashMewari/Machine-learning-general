import flask 
from flask import Flask,render_template,request,url_for
import pickle 
import pandas as pd


app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')




@app.route("/predict", methods=['GET','POST'])    
def predict():
	if(request.method == 'POST'):
		lsat = float(request.values['lstat'])
		rm = float(request.values['rm'])
		with open('linearmodel.sav', 'rb') as f:
			dt1 = pickle.load(f)
		value=dt1.predict([[lsat,rm]])
	return render_template('index.html',prediction_text="Your is Rs. {}".format(abs(value)))
	
if __name__ == '__main__':
	app.run(debug=True)