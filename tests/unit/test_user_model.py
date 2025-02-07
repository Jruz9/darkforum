from models import Users

def test_user():
    u = Users()
    u.username = 'egg'
    u.passcode = 'kjshgiuowenjk'
    assert u.username == 'egg'
    assert u.passcode == 'kjshgiuowenjk'