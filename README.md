# 📚 Book Recommender System

A simple **Flask-based Book Recommendation Web App** that suggests similar books based on user input.  
It uses precomputed similarity scores (via Machine Learning / collaborative filtering) to recommend books.

🔗 **Live Demo:** [Book Recommender on Render](https://book-recommender-eqxp.onrender.com/)

## Features

-  View Top 50 Popular Books  
-  Search and Get Similar Book Recommendations  
-  Built with Flask, Pandas, and NumPy    
-  Deployed on Render (Free Tier)


## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Data Handling:** Pandas, NumPy
- **Deployment:** Render

## How It Works

1. User enters a book name (e.g. *The Notebook*).  
2. The app finds similar books using a similarity matrix (`similarity_score.pkl`).  
3. Recommendations are displayed with book cover, author, rating, and votes.

## Installation (Run Locally)

1. Clone this repository:
   ```bash
   git clone https://github.com/chandnii96/Book-Recommender.git
   cd Book-Recommender
````

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate
````

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
````

4. Run the Flask app:
   ```bash
   python app.py
````
