from flask import Flask, render_template, request, redirect, url_for, flash

server = Flask(__name__)
server.secret_key = 'oogabooga33'  # Used for session management

# Dummy user data (username and password)
users = {
    "admin": "admin123",
    "user1": "passord123"
}

# Sample forum posts (in memory for now)
posts = [
    {'title': 'Velkommen', 'content': 'Første post her', 'author': 'admin'},
    {'title': 'Chill flask app', 'content': 'Ooga Booga', 'author': 'user1'}
]

@server.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            return redirect(url_for('index'))
        else:
            flash("Feil brukernavn eller passord. Venligst prøv igjen.", "danger")
            return redirect(url_for('login'))

    return render_template('login.html')

@server.route('/index')
def index():
    return render_template('index.html')

@server.route('/forum')
def forum():
    # Vis alle postene på forumet.
    return render_template('forum.html', posts=posts)

@server.route('/forum/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = 'admin'  # kun for testing
        
        # Legger til ny post til liste
        posts.append({'title': title, 'content': content, 'author': author})
        flash('Your post has been created!', 'success')
        return redirect(url_for('forum'))
    
    return render_template('new_post.html')

if __name__ == '__main__':
    server.run(debug=True)
