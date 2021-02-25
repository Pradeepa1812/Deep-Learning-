import numpy as np
import tensorflow as tf
import keras
from flask import Flask,request,url_for,render_template,redirect
from keras.models import load_model

app=Flask(__name__)
model_path='filename.h5'

#'''global graph
#from tensorflow.python.framework import ops
#graph=ops.reset_default_graph()'''
model=load_model(model_path)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        preg = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        bp = int(request.form['bloodpressure'])
        st = int(request.form['skinthickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])
        age = int(request.form['age'])
        
        #data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        
        my_prediction = model.predict([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        
        return render_template('results.html', prediction=my_prediction)


if __name__=='__main__':
    app.run(debug=True)

