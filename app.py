import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import streamlit as st

from flask import Flask, render_template,request
from model import Model
import pickle

app = Flask(__name__)

try:
    with open('objects/popular.pkl', 'rb') as f:
        popular_df = pickle.load(f)
        print("popular_df loaded successfully")
        print(popular_df.head())

    with open('objects/pt.pkl', 'rb') as f:
        pt = pickle.load(f)
        print("pt loaded successfully")
        print(pt.head())

    with open('objects/books.pkl', 'rb') as f:
        books = pickle.load(f)
        print("books loaded successfully")
        print(books.head())

    with open('objects/similarity_scores.pkl', 'rb') as f:
        similarity_scores = pickle.load(f)
        print("similarity_scores loaded successfully")
        print(similarity_scores)
except Exception as e:
    print(f"Error loading pickle files: {e}")

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    try:
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)

        print(data)
    except Exception as e:
        print(f"Error in recommendation process: {e}")
        data = []

    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)  
    # Using use_reloader=False to avoid the signal error
