from config.db.connection import create_connection

def get_user_by_username(connection, username):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    return cursor.fetchone()

def register_user(connection, username, password, email):
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
        (username, password, email)
    )
    connection.commit()