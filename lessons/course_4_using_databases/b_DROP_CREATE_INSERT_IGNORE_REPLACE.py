
import sqlite3
import xml.etree.ElementTree as ET

source = '../../data/sample/musical_library.xml'

connection = sqlite3.connect('../../data/output/track.sqlite')
cursor = connection.cursor()


cursor.executescript('''
                     
DROP TABLE IF EXISTS Artist;       
CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
                     
DROP TABLE IF EXISTS Album;
CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);
                     
DROP TABLE IF EXISTS Genre;
CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
                     
DROP TABLE IF EXISTS Track;
CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
)
                     
''')


tree = ET.parse(source)
tracks = tree.findall('dict/dict/dict')

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>


def lookup(data, key):
    found = False
    for entry in data:
        if found:
            return entry.text
        if entry.tag == 'key' and entry.text == key :
            found = True
    return None


for track in tracks:
    if (lookup(track,'Track ID') is None):
        continue

    name    = lookup(track, 'Name')
    artist  = lookup(track, 'Artist')
    album   = lookup(track, 'Album')
    genre   = lookup(track, 'Genre')
    count   = lookup(track, 'Play Count')
    rating  = lookup(track, 'Rating')
    length  = lookup(track, 'Total Time')


    if name is None or artist is None or album is None or genre is None:
        continue

    cursor.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', ( artist,))
    cursor.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cursor.fetchone()[0]

    cursor.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?,?)', (album, artist_id))
    cursor.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cursor.fetchone()[0]

    cursor.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', ( genre,))
    cursor.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cursor.fetchone()[0]


    cursor.execute(
        'INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)',
        (name, album_id, genre_id, length, rating, count)
    )

    connection.commit()

'''

Check output in DB Browser for SQLite:

SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3

'''