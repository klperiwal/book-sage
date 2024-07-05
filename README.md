# Book-Sage

<b>Dataset Link: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset</b>

## Overview:-
The Book-Sage is a book recommendation system which uses collaborative filtering-based system design to provide personalized recommendations to users based on their preferences and interactions. The system uses a combination of user ratings, book features, and similarity metrics to generate relevant and engaging recommendations.


## Features:-
- User Profiles: Capture user preferences and interactions with books.
- Collaborative Filtering: Identify similar users and books to make personalized recommendations.
- Cosine Similarity: Measure the similarity between user profiles and books using cosine similarity.
- Sparse Data Handling: Effective handling of sparse user-item interaction matrices.
- Scalability: Designed for scalability to handle large datasets efficiently.


## Working:-
<b>1- Collaborative Filtering: </b>
The system identifies similar users based on their rating patterns.
Collaborative filtering is used to recommend books liked by similar users.

<b>2- Cosine Similarity: </b>
Cosine similarity is employed to measure the similarity between user profiles and books.
It considers the angle between vectors, providing robust recommendations.

<b>3- Recommendation Generation: </b>
Based on user preferences and similarity metrics, the system generates personalized book recommendations.
Recommendations are presented to users through the system interface.

<br>

## Installation

To get started with <b>BookSage</b>, follow these steps:

1- Clone the repository from GitHub:
   ```bash
   git clone https://github.com/klperiwal/book-sage
   ```

2- Navigate to the project directory:

   ```bash
   cd book-sage
   ```

3- Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4- Install the books dataset from the given link:<br>
     <p> <b>Dataset Link: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset</b>
      <br> Add the dataset to the corresponding relative path: '__/Dataset/filename__'</p>
   
5- Run the app.py :

   ```bash
   python app.py
   ```
6- Start the Streamlit app to get the list of recommendation:
   ```bash
   streamlit run app.py
   ```
  Visit the app in your web browser to use it (Browser link: `http://localhost:8501`).
