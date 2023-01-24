import json
import sqlite3
from db_setup import setup_script


conn = sqlite3.connect("rosterdb.sqlite")
cur = conn.cursor()

cur.executescript(setup_script)

file_name = input("Enter a file name:")
if len(file_name) < 1:
    file_name = "roster_data_sample.json"

with open(f"{file_name}", "r") as str_data:
    json_data = json.loads(str_data)
    for entry in json_data:
        name = entry[0]
        title = entry[1]

        print((name, title))
        cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)", (name,))
        cur.execute("SELECT if FROM User WHERE name = ?", (name,))
        user_id = cur.fetchone()[0]

        cur.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (title,))
        cur.execute("SELECT if FROM Course WHERE title = ?", (title,))
        course_id = cur.fetchone()[0]
        
        cur.execute("""INSERT OR REPLACE INTO Member (user_id, course_id)
                    VALUES (?,?)""", (user_id, course_id))

        conn.commit()