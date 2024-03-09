
import sqlite3

connection = sqlite3.connect('../../data/output/email.sqlite')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

handle = open('../../data/sample/mbox.txt')


for line in handle:
    if not line.startswith('From: '):
        continue

    email = line.split()[1]
    domain = email.split('@')[1]

    cursor.execute(
        'SELECT count FROM Counts WHERE org = ? ',
        (domain,)
    )

    if cursor.fetchone() is None:
        cursor.execute(
            'INSERT INTO Counts (org, count) VALUES (?, 1)',
            (domain,) # tuple of one element
        )
    else:
        cursor.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?',
            (domain,)
        )

    connection.commit()


for row in cursor.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'):
    print(str(row[0]), row[1])

cursor.close()
