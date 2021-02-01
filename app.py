from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = "This_is_a_secret_key"

cities = [line.strip() for line in open('city.txt', encoding='utf-8').readlines()]
friends = ['Pete', 'Sue', 'Alice', 'Bob']

@app.route('/')
def index():
    if 'search_result' in session:
        search_result = session.pop('search_result')
    else:
        search_result = []
    return render_template('index.html', result=search_result)


@app.route('/search', methods=['POST'])
def search():
    search_field = request.form['search']
    search_result = [city for city in cities if search_field in city]
    session['search_result'] = search_result
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username.lower() != 'admin' or password.lower() != 'superstar':
        return redirect(url_for('index'))
    else:
        session['username'] = username
        return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return render_template('profile.html', username=session['username'], friends=friends)


@app.route('/add_friend', methods=['POST'])
def add_friend():
    friends.append(request.form['friend'])
    return redirect(url_for('profile'))



if __name__ == '__main__':
    app.run()
