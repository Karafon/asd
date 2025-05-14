import csv
import sqlite3

conn = sqlite3.connect('Zen.db')
c = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command (id INTEGER PRIMARY KEY, name VARCHAR(100), path VARCHAR(255))"
# c.execute(query)


# query = "INSERT INTO sys_command VALUES (null, 'discord', 'C:\\Users\\hasan\\AppData\\Local\\Discord\\app-1.0.9190\\Discord.exe')"
# c.execute(query)
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command (id INTEGER PRIMARY KEY, name VARCHAR(100), url VARCHAR(255))"
# c.execute(query)

# query = "INSERT INTO web_command VALUES (null, 'youtube', 'https://www.youtube.com/')"
# c.execute(query)
# conn.commit()


# app_name = "discord"
# c.execute("SELECT path FROM sys_command WHERE name=?", (app_name,))
# result = c.fetchall()
# print(result)

# c.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# desired_columns_indices = [0, 18]

# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         c.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# conn.commit()
# conn.close()

