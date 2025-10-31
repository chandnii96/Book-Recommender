from flask import Flask, render_template, request, session, redirect, url_for
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Secret key for session management

# Load your data outside of route functions
popular_df = pd.read_pickle('popular.pkl')
pt = pd.read_pickle('pt.pkl')
books = pd.read_pickle('books.pkl')
similarity_score = pd.read_pickle('similarity_score.pkl')

# Dummy user data for demonstration
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        logged_in = True
    else:
        username = None
        logged_in = False

    return render_template('index.html', username=username, logged_in=logged_in,
                           image=list(popular_df['Image-URL-M'].values),
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           votes=list(popular_df['num_rating'].values),
                           rating=list(popular_df['avg_rating'].values))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input').strip().lower()

    # Find all book titles that contain the user's input (case-insensitive)
    matches = [title for title in pt.index if user_input in title.lower()]

    if not matches:
        return render_template(
            'recommend.html',
            error=f"No books found matching '{user_input}'. Please try another title."
        )

    # Use the first closest match
    matched_title = matches[0]

    index = np.where(pt.index == matched_title)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_score[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:7]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return render_template('recommend.html', data=data, search_query=matched_title)


if __name__ == '__main__':
    app.run(debug=True)
