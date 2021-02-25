import numpy as np
import pandas as pd
import pickle
from flask import Flask,request,render_template,url_for
import numpy as np
import keras
import joblib
from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import text,sequence

app=Flask(__name__)
model=load_model('model_file.h5')

@app.route('/')
def home():
    return render_template('toxic.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        sample=request.form['sample']
        tok = Tokenizer(num_words=25000)
        tok.fit_on_texts(list(sample))
        seqt = tok.texts_to_sequences(sample)
        padt = sequence.pad_sequences(seqt, maxlen=150)
        my_prediction=model.predict([padt])[0]
        return render_template('output_toxic.html',pred=my_prediction,t=sample)
        




if __name__=='__main__':
    app.run(debug=True)
