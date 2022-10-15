from urllib import response
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
  response= requests.get("https://api.themoviedb.org/3/movie/{}?api_key=586a1ea1e9b2264150386e47403bb220&language=en-US".format(movie_id))
  data=response.json()
#   print(data)
  return   "http://image.tmdb.org/t/p/w500"+data['poster_path']


def recommend(movie):
   movie_index=movies[movies['title']==movie].index[0]
   distances = similarity[movie_index]
#     we are aimimg at sorting the movies based on similarity but in this process we loose the original index of the movie hence tp resolve this we use enumerate function
   movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
   recommended_movies=[] 
   recommended_movies_posters=[]
   for i in movie_list:
      movie_id=movies.iloc[i[0]].movie_id
      recommended_movies.append(movies.iloc[i[0]].title)
      recommended_movies_posters.append(fetch_poster(movie_id))  
   return recommended_movies,recommended_movies_posters


movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity= pickle.load(open('similarity.pkl','rb'))

st.title('Movie Reccomendations System ')
selected_movie_names = st.selectbox(
'Got your Mood!! What would you like to watch?',
 movies['title'].values)

# st.write('You selected:', option)


if st.button('Reccomend'):
   names,posters=recommend(selected_movie_names)
   
   col1, col2, col3, col4, col5 = st.columns(5)

   with col1:
      st.text(names[0])
      st.image(posters[0])

   with col2:
      st.text(names[1])
      st.image(posters[1])

   with col3:
      st.text(names[2])
      st.image(posters[2])
   with col4:
       st.text(names[3])
       st.image(posters[3])
   with col5:
       st.text(names[4])
       st.image(posters[4])