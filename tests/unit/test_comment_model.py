from models import Comments

def test_comment():
    c = Comments()
    c.comment_text = 'this is a comment'
    c.comment_author = 'egg'
    assert c.comment_text == 'this is a comment'
    assert c.comment_author == 'egg'