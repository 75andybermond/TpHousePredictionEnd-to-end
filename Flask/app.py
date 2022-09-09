from flask import Flask,render_template,request
import pickle
import numpy as np


app = Flask('__name__')
model=pickle.load(open('model_no_dummies.pkl','rb'))

@app.route('/')
def hello():
     return render_template("home.html", message = "House price prediction by Andy ! ")

@app.route('/result',methods=["POST"])
def predict():
        feature=[(float(x)) for x in request.form.values()]
        print(feature)
        feature_final=np.array(feature).reshape(1,-1)
        print(feature_final)
        prediction=model.predict(feature_final)
        print(prediction)
        return render_template('home.html',prediction_text="Prediction is : {}$".format(int(prediction)))


if(__name__=='__main__'):
    app.run(debug=True)