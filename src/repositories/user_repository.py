from models import db, Users, Posts, Comments

class UserRepository:
    #Loads user information from an ID
    def get_user_by_id(self, users_id):
        single_user = Users.query.get_or_404(users_id)

        return single_user
    def get_all_users(self):
        getAll = Users.query.all()

        return getAll

    #Creates a new user and saves it to the database
    def create_user(self, username, passcode):
        new_user = Users(username = username, passcode = passcode)

        db.session.add(new_user)
        db.session.commit()

        return new_user

    #Determines if user is an existing user
    def login(self, temp_username, temp_passcode):
        confirmed_user = Users.query.filter_by(username = temp_username, passcode = temp_passcode).first()

        if confirmed_user.username == temp_username and confirmed_user.passcode == temp_passcode:
            is_user = True
        else:
            is_user = False

        return is_user


    def search_post(self, title):
        title_search=title
        match=Posts.query.filter(Posts.post_title.like("%"+title_search+"%")).all()

        return match

    #Creates a post
    def create_post(self, post_title, post_text, post_author, post_created_date):
        new_post = Posts(post_title = post_title, post_text = post_text, post_author = post_author, post_created_date = post_created_date)

        db.session.add(new_post)
        db.session.commit()

        return new_post

    #Loads post information from an ID
    def get_post_by_id(self, posts_id):
        single_post= Posts.query.get_or_404(posts_id)

        return single_post

    #Grabs all posts
    def get_all_posts(self):
        all_posts = Posts.query.all()
        return all_posts


    def delete_post(self,user_id):
        Posts.query.filter_by(user_id).delete()
        db.session.commit()

    def update_post_comment(self,user_id,user_comment):
        user_post=Posts.query.get(user_id)
        user_post.post_comment = user_comment
        db.session.commit()
    
    #Creates a comment
    def create_comment(self, comment_text, comment_author, comment_posts_id):
        new_comment = Comments(comment_text = comment_text, comment_author = comment_author, comment_posts_id = comment_posts_id)

        db.session.add(new_comment)
        db.session.commit()

        return 
        
    #Grabs a comment
    def get_comment_by_id(self, comments_id):
        comment = Users.query.get_or_404(comments_id)

        return comment

    #Grabs all comments
    def get_all_comments(self):
        all_comments = Comments.query.all()

        return all_comments

user_repository_singleton = UserRepository()
