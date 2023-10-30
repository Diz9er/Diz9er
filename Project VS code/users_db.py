import sqlite3

conn = sqlite3.connect('users1.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY,
                                    login TEXT,
                                    password TEXT,
                                    email TEXT)''')

cur.execute("INSERT INTO users (login, password, email) VALUES ('user1', 'password1', 'user1@example.com')")
cur.execute("INSERT INTO users (login, password, email) VALUES ('user2', 'password2', 'user2@example.com')")
cur.execute("INSERT INTO users (login, password, email) VALUES ('user3', 'password3', 'user3@example.com')")

conn.commit()
cur.close()
conn.close()