import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER
)
''')

conn.commit()

users = [
    ('Ania', 'Ania@wp.pl', 46),
    ('Kamil', 'Kamil@wp.pl', 26),
    ('Kaska', 'kaska@o2.pl', 10),
]

cursor.executemany('INSERT INTO users (name, email, age) VALUES (?, ?, ?)', users)
conn.commit()

print('Użytkownicy')
cursor.execute('SELECT * FROM users')
for row in cursor.fetchall():
    print(row)

cursor.execute('UPDATE users SET age = 30 WHERE name = "Kamil"')
cursor.execute('DELETE FROM users WHERE age = 46')
conn.commit()

print('Użytkownicy')
cursor.execute('SELECT * FROM users')
for row in cursor.fetchall():
    print(row)

conn.close()