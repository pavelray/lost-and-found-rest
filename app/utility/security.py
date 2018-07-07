from models.user import UserModel

users = [
    UserModel('1','pavel','1234')
]

username_mapping = {u.user_name: u for u in users }
userid_mapping = {u.id: u for u in users}

def authenticate(user_name,password):
    user = username_mapping.get(user_name,None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id=payload['identity']
    return userid_mapping.get(user_id,None)