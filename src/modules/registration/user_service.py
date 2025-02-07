from config.db.connection import execute_query

def get_user_by_username(connection, username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return execute_query(connection, query)

def register_user(connection, username, password, email):
    query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')"
    print(query)
    return execute_query(connection, query)