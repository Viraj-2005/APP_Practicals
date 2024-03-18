import sqlite3
# (A) Connecting to Database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# (B) Creating a Table
cursor.execute('''CREATE TABLE if not exists users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# (C) Inserting Data into the table
cursor.execute("INSERT INTO users(name, age) VALUES(?, ?)",('John Dae','25'))
cursor.execute("INSERT INTO users(name, age) VALUES(?, ?)",('Jane Smith','30'))

# Fetching data to verify insertion
cursor.execute("SELECT * FROM users")
print("Data after Fetching: ")
print(cursor.fetchall())

# Updating data in the table
cursor.execute("UPDATE users SET age = 26 WHERE name = 'Jphn Dae'")

# Fetching data to verify update
cursor.execute("SELECT * FROM users")
print("Data after updating John Dae's age: ")
print(cursor.fetchall())

# Dropping the table
cursor.execute("DROP TABLE IF EXISTS users")

# Committing changes and closing connection
conn.commit()
conn.close()
