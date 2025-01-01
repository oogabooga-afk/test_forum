from flask import Flask, render_template, request, redirect, url_for, flash

server = Flask(__name__)
server.secret_key = 'oogabooga33'  # bruker for session håndtering

# Dummy bruker data (brukernavn og passord)
users = {
    "admin": "admin123",
    "user1": "passord123"
}

# samplet forum post (i minnet for nå)
posts = [
    {'id': 1, 'title': 'Velkommen', 'content': 'nytt forum', 'author': 'admin', 'comments': []},
    {'id': 2, 'title': 'Dagens spørsmål', 'content': 'Drakk du mye denne nyttårsaften? Hvorfor/Hvorfor ikke?', 'author': 'user1', 'comments': []}
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
        author = 'admin'  # Kun for testing - Erstatt med dynamisk bruker håndtering 
    
        # gir en ny ID til hver post.
        new_id = len(posts) + 1
        posts.append({'id': new_id, 'title': title, 'content': content, 'author': author, 'comments': []})
        flash('Your post has been created!', 'success')
        return redirect(url_for('forum'))
    
    return render_template('new_post.html')

@server.route('/forum/comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    comment_content = request.form['comment']
    author = 'admin'  # kun for testing - fiks dynamisk bruker håndtering 

    # Finner posten og sender kommentar
    for post in posts:
        if post['id'] == post_id:
            post['comments'].append({'author': author, 'content': comment_content})
            break

    flash('Your comment has been added!', 'success')
    return redirect(url_for('forum'))


if __name__ == '__main__':
    server.run(debug=True)
