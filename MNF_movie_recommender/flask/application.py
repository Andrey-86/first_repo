from flask import Flask, render_template, request
import recommender


app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies')
def movies():
    num = 3
    return render_template('movies.html', num_html=num)

@app.route('/results')
def results():
    user_input = dict(request.args)
    user_movies = list(user_input.values())[::2]
    user_ratings = list(user_input.values())[1::2]
    movies_list = recommender.nmf(user_movies, user_ratings)
    return render_template('results.html', movies_html = movies_list)

@app.route('/name/<name>')
def greeting(name):
    return f"<h1>Hello, {name}!</h1>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
