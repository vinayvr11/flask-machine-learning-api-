# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))



posts = [
        {'Name':'Vinay',
         'Work':'Scientist',
         'Billionaire':'20$ billion'}

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return '<h1>About Page</h1>'


@app.route('/predict',methods=['POST'])
def predict():
    experience = [int(x) for x in request.form.values()]
    final_feature = [experience]
    prediction = model.predict(final_feature)
    output =  np.round(prediction,2)
   
    return render_template('home.html',prediction_text='Employee salary Should be $ {}'.format(output))
    