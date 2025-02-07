from models import Posts

def test_post():
    p = Posts()
    p.post_author = 'egg'
    p.post_text = 'hello, welcome to my first post'
    p.post_title = 'this is a post'