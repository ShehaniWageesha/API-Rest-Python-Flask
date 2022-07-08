from db import get_db


def insert_user(name, email, phone):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(name, email, phone) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, email, phone])
    db.commit()
    return True


def update_user(id, name, email, phone):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE users SET name = ?, email = ?, phone = ? WHERE id = ?"
    cursor.execute(statement, [name, email, phone, id])
    db.commit()
    return True


def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM users WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, email, phone FROM users WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_users():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, email, phone FROM users"
    cursor.execute(query)
    return cursor.fetchall()
