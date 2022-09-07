import pickle
import flask import Flask,request,app,jsonsify,url_for, render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model 
model=pickle.load(open('MLPregressorModel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    