import errno
from gzip import READ
from os import abort, getenv
from flask import Flask, redirect, render_template, request, url_for
from sqlalchemy import false
from src.repositories.user_repository import user_repository_singleton
from models import Posts, Users, db
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("CLEARDB_DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) 

#Global variables
logged_in_user = None
logged_in = False
clicked = False

#Homepage link
@app.get('/')
def index():
    all_posts = user_repository_singleton.get_all_posts()
    all_comments = user_repository_singleton.get_all_comments()
    
    return render_template('index.html', posts = all_posts, logged_in_user = logged_in_user, num_post = len(all_posts), num_comments = len(all_comments), logged_in = logged_in)

#Delete link
@app.get('/delete_post/<int:posts_id>')
def delete_post(posts_id):
    post = Posts.query.filter_by(posts_id = posts_id).first()

    db.session.delete(post)
    db.session.commit()

    return redirect('/')

#Edit link
@app.get('/edit_post/new/<int:posts_id>')
def edit_post_form(posts_id):
    changed_post = user_repository_singleton.get_post_by_id(posts_id)

    return render_template('edit_post.html', post = changed_post, logged_in_user = logged_in_user, logged_in = logged_in)

@app.post('/edit_post/<int:posts_id>')
def edit_post(posts_id):
    changed_post = user_repository_singleton.get_post_by_id(posts_id)

    changed_post_title = request.form.get('post_title', '')
    changed_post_text = request.form.get('post_text','')

    changed_post.post_title = changed_post_title
    changed_post.post_text = changed_post_text

    db.session.add(changed_post)
    db.session.commit()

    return redirect('/')

#Post link
@app.get('/post/<int:posts_id>')
def post_form(posts_id):
    post = user_repository_singleton.get_post_by_id(posts_id)
    all_comments = user_repository_singleton.get_all_comments()
 
    return render_template('post.html', post = post, comments = all_comments, logged_in_user = logged_in_user, logged_in = logged_in, clicked = clicked)

@app.post('/post/<int:posts_id>')
def post_like_dislike(posts_id):
    post = user_repository_singleton.get_post_by_id(posts_id)
    all_comments = user_repository_singleton.get_all_comments()

    global clicked
    clicked = True


    return render_template('post.html', post = post, comments = all_comments, logged_in_user = logged_in_user, logged_in = logged_in, clicked = clicked)

#Create comment link
@app.post('/create_comment/<int:posts_id>')
def create_comment(posts_id):
    comment_text = request.form.get('comment_text', '')

    if comment_text == '':
        abort(400)

    new_comment = user_repository_singleton.create_comment(comment_text, logged_in_user.username, posts_id)
    
    return redirect(f'/post/{posts_id}')

#Create post Link
@app.get('/create_post/new')
def create_post_form():
    return render_template('create_post.html', logged_in_user = logged_in_user, logged_in = logged_in)

@app.post('/create_post')
def create_post():
    post_title = request.form.get('post_title','')
    post_text = request.form.get('post_text','')

    if post_title == '' or post_text == '':
        abort(400)
    
    current_date = date.today()

    new_post = user_repository_singleton.create_post(post_title, post_text, logged_in_user.username, current_date)

    return redirect(f'/post/{new_post.posts_id}')

#Logout link
@app.get('/logout')
def logout():
    global logged_in
    logged_in = False

    global logged_in_user
    logged_in_user = None

    return redirect('/')

#Login link
@app.route('/login', methods=["GET","POST"])
def login():
    error = None

    if request.method =='POST':
        username = request.form.get('username', '')
        passcode = request.form.get('passcode', '')
        is_user = user_repository_singleton.login(username, passcode)

        if is_user != True:
            error = 'Invalid response, please try again.'
        else:
            confirmed_user = Users.query.filter_by(username = username, passcode = passcode).first()

            global logged_in_user 
            logged_in_user = confirmed_user

            global logged_in
            logged_in = True

            return redirect('/')

    return render_template("login.html", error = error, logged_in_user = logged_in_user, logged_in = logged_in)

#Register link
@app.get('/register/new')
def register_form():
    return render_template("registration.html", logged_in_user = logged_in_user, logged_in = logged_in)

@app.post('/register')
def register():
    error = None
    username = request.form.get('username', '')
    passcode = request.form.get('passcode', '')

    if username == '' or passcode == '':
        error = 'You have not filled in your information'
    else:
        created_user = user_repository_singleton.create_user(username, passcode)
        return redirect('/')

    return render_template('registration.html', error = error, logged_in_user = logged_in_user, logged_in = logged_in)


@app.get('/post/search')
def search_for_forum():
    found_posts=[]
    search_term= request.args.get('forumsearch','')
    if search_term != '':
        found_posts=user_repository_singleton.search_post(search_term)

    return render_template('search.html',search_active=True,posts=found_posts,search_query=search_term, logged_in_user = logged_in_user, logged_in = logged_in)
    
if __name__ == '__main__':
    app.run()