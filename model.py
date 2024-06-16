import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split



class Model():
    def __init__(self) -> None:
        print('init running')
        books= pd.read_csv("Datasets/Books.csv")
        users= pd.read_csv("Datasets/Users.csv")
        ratings= pd.read_csv("Datasets/Ratings.csv")
        name_rate= ratings.merge(books, on='ISBN')

        num_rating= name_rate.groupby('Book-Title').count()['Book-Rating'].reset_index()
        num_rating.rename(columns={'Book-Rating': 'Num-Rate'}, inplace=True)

        avg_rating= name_rate.groupby('Book-Title')['Book-Rating'].mean().reset_index()
        avg_rating.rename(columns={'Book-Rating': 'Avg-Rate'}, inplace=True)

        final_df= num_rating.merge(avg_rating, on='Book-Title')
        final_df= final_df[final_df['Num-Rate'] >= 250].sort_values('Avg-Rate', ascending=False).head()

        final_df= final_df.merge(books, on='Book-Title').drop_duplicates('Book-Title')[['Book-Title', 'Book-Author', 'Num-Rate', 'Avg-Rate', 'Image-URL-M']]
        x= name_rate.groupby('User-ID').count()['Book-Rating'] > 200
        literate_ppl= x[x].index
        newrating= name_rate[name_rate['User-ID'].isin(literate_ppl)]

        y = newrating.groupby('Book-Title').count()['Book-Rating'] >= 50
        famousbooks = y[y].index

        final_ratings = newrating[newrating['Book-Title'].isin(famousbooks)]
        df_final = final_ratings.pivot_table(index='User-ID', columns='Book-Title', values='Book-Rating').fillna(0)

        self.df_final = df_final
        self.same_scores = cosine_similarity(df_final)

    def recommend(self, book_name):
        if book_name in self.df_final.columns:
            index = np.where(self.df_final.columns == book_name)[0][0]
            same_item = sorted(list(enumerate(self.same_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

            data = []  # For storing the book information
            for i in same_item:
                item = []
                temp = self.df_final.columns[i[0]]
                item.extend([temp, self.df_final[temp].mean(), self.df_final[temp].count()])
                data.append(item)
            return data
        else:
            return f"The book '{book_name}' is not found in the DataFrame."

# Example usage
model = Model()
recommendations = model.recommend('The Da Vinci Code')
print(recommendations)
