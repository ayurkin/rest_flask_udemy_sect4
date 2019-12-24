from user import User
from werkzeug.security import safe_str_cmp
# users = [
#     {
#         'id': 1,
#         'username': 'bob',
#         'password': 'qwert'
#     }
# ]
users = [
    User(1, 'bob', 'qwert')
]
username_mapping = {u.username: u for u in users}

# username_mapping = {'bob': {
#     'id': 1,
#     'username': 'bob',
#     'password': 'qwert'
# }
# }
userid_mapping = {u.id: u for u in users}
# userid_mapping = {1: {
#     'id': 1,
#     'username': 'bob',
#     'password': 'qwert'
# }
# }


def authenticate(username, password):
    user = username_mapping.get(username, None)
    # if user and user.password == password:
    if user and safe_str_cmp(user.password, password):
        return user


def identify(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)



