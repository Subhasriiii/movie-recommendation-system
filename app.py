import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🎬 Movie Recommendation System")
st.write("Enter a movie name to get top 10 similar recommendations!")

@st.cache_resource
def load_data():
    movies = pd.read_csv('movies.csv')
    movies['genres'] = movies['genres'].str.replace('|', ' ', regex=False)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return movies, cosine_sim

movies, cosine_sim = load_data()

def get_recommendations(title):
    matches = movies[movies['title'].str.contains(title, case=False, na=False)]
    if matches.empty:
        return None
    idx = matches.index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].reset_index(drop=True)

movie_name = st.text_input("Enter Movie Name", placeholder="e.g. Toy Story, Batman")

if st.button("Get Recommendations 🎯"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name!")
    else:
        results = get_recommendations(movie_name)
        if results is None:
            st.error("Movie not found! Try another name.")
        else:
            st.success(f"Top 10 movies similar to '{movie_name}':")
            for i, title in enumerate(results, 1):
                st.write(f"{i}. {title}")
