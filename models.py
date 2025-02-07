from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, false, null

db = SQLAlchemy()

#Users database
class Users(db.Model):
    username = db.Column(db.String, nullable = False)
    passcode = db.Column(db.String, nullable = False)
    users_id = db.Column(db.Integer, primary_key = True)

    def __repr__(self):
        return f'Users({self.username}, {self.passcode}, {self.users_id})'

#Post database
class Posts(db.Model):
    posts_id = db.Column(db.Integer, primary_key = True)
    post_title = db.Column(db.String, nullable = False)
    post_text = db.Column(db.String, nullable = False)
    #post_likes = db.Column(db.Integer)
    #post_dislikes = db.Column(db.Integer)
    post_created_date = db.Column(db.String, nullable = False)
    post_author = db.Column(db.String, db.ForeignKey(Users.users_id), nullable = True)
    user = db.relationship('Users', foreign_keys = 'Posts.post_author')

    def __repr__(self):
        return f'Posts({self.posts_id}, {self.post_title}, {self.post_text})'

#Comments database
class Comments(db.Model):
    comments_id = db.Column(db.Integer, primary_key = True)
    comment_text = db.Column(db.String, nullable = False)
    comment_author = db.Column(db.Integer, db.ForeignKey(Users.users_id), nullable = True)
    user = db.relationship('Users', foreign_keys = 'Comments.comment_author')
    comment_posts_id = db.Column(db.Integer, db.ForeignKey(Posts.posts_id), nullable = True)
    post = db.relationship('Posts', foreign_keys = 'Comments.comment_posts_id')



    def __repr__(self):
        return f'Comments({self.comments_id}, {self.comment_text})'