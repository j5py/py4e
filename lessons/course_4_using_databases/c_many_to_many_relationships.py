
import json
import sqlite3


connection = sqlite3.connect('../../data/output/roster.sqlite')
cursor = connection.cursor()


cursor.executescript('''

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);
                     
CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);
                     
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)

''')


for entry in json.loads(open('../../data/sample/roster_data.json').read()):

    cursor.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (entry[0],))
    cursor.execute('SELECT id FROM User WHERE name = ?', (entry[0],))
    user_id = cursor.fetchone()[0]

    cursor.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (entry[1],))
    cursor.execute('SELECT id FROM Course WHERE title = ?', (entry[1],))
    course_id = cursor.fetchone()[0]


    cursor.execute(
        'INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)',
        (user_id, course_id, entry[2])
    )

    connection.commit()

'''

Check output in DB Browser for SQLite:


SELECT User.name, Course.title, Member.role FROM
  User JOIN Member JOIN Course
  ON User.id = Member.user_id AND Member.course_id = Course.id
      ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

Zian|si106|0
Zhuo|si422|0


SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
  User JOIN Member JOIN Course
  ON User.id = Member.user_id AND Member.course_id = Course.id
      ORDER BY X LIMIT 1;

'''
