import gzip, pickle

import pandas as pd
import streamlit as st


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []


    for i in movies_list:

        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb') )
movies = pd.DataFrame(movies_dict)
movies.head()

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
movie_list = movies['title'].values
selected_movie_name = st.selectbox(
'How would you like to be contacted',
movie_list
)

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
       st.write(i)


