
import sqlite3
import json
import codecs


connection = sqlite3.connect('../../../data/output/locations.sqlite')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Locations')


handle = codecs.open('../../../data/output/locations.js', 'w', 'utf-8')
handle.write('const locations = [\n')
count = 0


for row in cursor :

    try:
        js = json.loads(str(row[1].decode()))
    except:
        continue

    if not('status' in js and js['status'] == 'OK') : continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    if lat == 0 or lng == 0 :
        continue

    location = js['results'][0]['formatted_address']
    location = location.replace("'", '')

    try :
        count += 1
        if count > 1 :
            handle.write(',\n')
        handle.write('    [' + str(lat) + ',' + str(lng) + ", '" + location + "']")
        print(location, lat, lng)
    except:
        continue


handle.write('\n];')
cursor.close()
handle.close()


print(count, 'records written to locations.js')
print('Open locations.html to view the data in a browser')
