
import sys
import urllib.request, urllib.parse, urllib.error
import sqlite3
import time
import json
import http
import ssl


test = ssl.create_default_context()
test.check_hostname = False
test.verify_mode = ssl.CERT_NONE


# http.client.HTTPConnection.debuglevel = 1


# key = 'AIzaSy___IDByT70'
key = False
if key is False:
    key = 42
    api = 'https://py4e-data.dr-chuck.net/geojson?'
else :
    api = 'https://maps.googleapis.com/maps/api/geocode/json?'


connection = sqlite3.connect('../../../data/output/locations.sqlite')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Locations (location TEXT, geodata TEXT)')


count = 0
locations = open('../../../data/sample/locations.data')
for line in locations:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break


    location = line.strip()
    cursor.execute(
        'SELECT geodata FROM Locations WHERE location= ?',
        (memoryview(location.encode()), )
    )

    try:
        data = cursor.fetchone()[0]
        print('Found in database', location)
        continue
    except:
        pass


    parameters = dict()
    parameters['address'] = location
    if key is not False: parameters['key'] = key

    url = api + urllib.parse.urlencode(parameters)
    print('Retrieving', url)

    data = urllib.request.urlopen(url, context=test)
    data = data.read().decode()
    print(data)
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))


    try:
        js = json.loads(data)
    except:
        print(data) # in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break


    cursor.execute(
        'INSERT INTO Locations (location, geodata) VALUES (?, ?)',
        (memoryview(location.encode()), memoryview(data.encode()))
    )
    connection.commit()


    count += 1
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)


print('Run dump.py to read the data from the database so you can vizualize it on a map')
