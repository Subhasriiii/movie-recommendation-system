# 🎬 Movie Recommendation System

A content-based movie recommendation web app built with Python and Streamlit.
Enter any movie name and get top 10 similar movie recommendations instantly!

## 🌐 Live Demo
👉 https://movie-recommendation-system-ntfm2n9fyi2mu3tge6uhzn.streamlit.app

## 📌 About the Project
This project builds a content-based filtering system using the MovieLens 
dataset. It analyzes movie genres to find and recommend similar movies 
using TF-IDF vectorization and Cosine Similarity.

## ⚙️ How It Works
1. Movie genres are extracted from the MovieLens dataset
2. TF-IDF vectorization converts genres into numerical feature vectors
3. Cosine Similarity measures the similarity between all movies
4. When a user enters a movie name, the top 10 most similar 
   movies are returned

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Pandas, Scikit-learn, NumPy
- **Algorithm:** TF-IDF Vectorization + Cosine Similarity
- **Web App:** Streamlit
- **Dataset:** MovieLens Small Dataset (Kaggle)

## 📂 Project Structure
movie-recommendation-system/
├── app.py            # Streamlit web app
├── movies.csv        # MovieLens dataset
└── requirements.txt  # Required libraries

## 🚀 How to Run Locally
# Clone the repo
git clone https://github.com/Subhasriiii/movie-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

## 📸 Features
- Enter any movie name in the search box
- Get top 10 similar movie recommendations
- Clean and simple web interface
- Fast real-time recommendations
