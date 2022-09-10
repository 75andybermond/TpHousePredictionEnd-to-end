from flask import Flask,render_template,request
from sklearn.preprocessing import MinMaxScaler
import pickle
import numpy as np
import pandas as pd


app = Flask('__name__')
model=pickle.load(open('model_no_dummies.pkl','rb'))

raw_data = pd.read_csv('df_nodummies.csv')
X = raw_data.loc[:, raw_data.columns != 'price']
scaler = MinMaxScaler()
scaler.fit(X.to_numpy())

@app.route('/')
def hello():
     return render_template("home.html", message = "House price prediction by Andy! ")

@app.route('/result',methods=["POST"])
def predict():
        feature=[(float(x)) for x in request.form.values()]
        feature = np.array(feature).reshape(1,-1)
        print("raw feature")
        print(feature)
        
        feature = scaler.transform(feature)
        print("transformed feature")
        print(feature)

        prediction=model.predict(feature)
        print(prediction)
        return render_template('home.html',prediction_text="Prediction is : {}$".format(int(prediction)))


if(__name__=='__main__'):
    app.run(debug=True)