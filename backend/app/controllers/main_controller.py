from app import app
from app.views import main

app.add_url_rule('/', 'index', main.index)
app.add_url_rule('/users', 'get_users', main.get_users, methods=['GET'])
app.add_url_rule('/users', 'add_user', main.add_user, methods=['POST'])
