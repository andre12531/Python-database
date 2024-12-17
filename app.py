import os
from flask import Flask, jsonify, request, g
from flask_httpauth import HTTPBasicAuth
from database import get_db_session, fetch_users, User
import json
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = "очень_надежный_случайно_сгенерированный_ключ"


# Загрузка конфигурации (та же, что и раньше - без паролей)

app.teardown_appcontext(lambda x: get_db_session(config.get("database_url")).remove())

# Аутентификация пользователей (замените на вашу безопасную систему аутентификации)

users_db = { #ЗАМЕНИТЕ на безопасное хранение и извлечение хешированных паролей из вашей базы данных
    "user1@example.com": generate_password_hash("password1"),
    "user2@example.com": generate_password_hash("password2"),
    "user3@example.com": generate_password_hash("password3"),
    "user4@example.com": generate_password_hash("password4"),
    "user5@example.com": generate_password_hash("password5"),
    "user6@example.com": generate_password_hash("password6"),
    "user7@example.com": generate_password_hash("password7"),
    "user8@example.com": generate_password_hash("password8"),
    "user9@example.com": generate_password_hash("password9"),
    "user10@example.com": generate_password_hash("password10"),

}

@auth.verify_password
def verify_password(email, password):
    if email in users_db and check_password_hash(users_db.get(email), password):
        return email
    return None



@app.route('/api/users', methods=['GET'])
@auth.login_required
def api_users():
    session = g.session
    email = request.args.get('email')
    ip_address = request.args.get('ip_address')
    results = fetch_users(session, email, ip_address)
    data = [{'id': r.id, 'email': r.email, 'ip_address': r.ip_address} for r in results]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
