import pandas as pd
import numpy as np
import streamlit as st

from flask import Flask, render_template
from model import Model

app=Flask(__name__,template_folder='web_codes')
model = Model()
def get_recommendations():
    recommend = model.recommend('Animal Farm')
    return recommend

@app.route('/recommender.ejs')
# @app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/recommendations')
def recommendations():
    recommended_books= get_recommendations()
    try:
        return render_template('recommender.html', recommended_books=recommended_books)
    except:
        return f"The catch value doesnot exist."

if __name__ == '__main__':
    app.run(debug=True)