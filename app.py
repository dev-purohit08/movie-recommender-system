import streamlit as st
import pickle
import pandas as pd
import requests


similarity = pickle.load(open('sim.pkl','rb'))



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        #fetch poster
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict= pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('Movie Recommender System')

selected = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

st.write('You selected:', selected)

if st.button('Recommend'):
    recommendations=recommend(selected)
    for i in recommendations:
        st.write(i)
else:
    st.write('')