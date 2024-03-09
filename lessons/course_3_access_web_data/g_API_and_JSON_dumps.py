
import urllib.request, urllib.parse, urllib.error
import json
import ssl


key = False # or your Google Places API key
if key is False:
    key = 42
    api = 'http://py4e-data.dr-chuck.net/json?'
else:
    api = 'https://maps.googleapis.com/maps/api/geocode/json?'


test = ssl.create_default_context()
test.check_hostname = False
test.verify_mode = ssl.CERT_NONE


# Prompt for a location, get JSON from the web service and parse that data

while True:
    string = input('Enter location: ')

    if len(string) == 0:
        string = 'University of Mumbai'
    elif string == 'done':
        break


    query = dict()
    query['address'] = string
    if key is not False: query['key'] = key

    handle = urllib.request.urlopen(api + urllib.parse.urlencode(query), context=test)
    data = handle.read().decode()

    
    try:
        report = json.loads(data)
    except:
        report = None

    if not report or 'status' not in report or report['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue


    # Then retrieve the first place_id (within Google Maps) from the JSON

    # print(json.dumps(report, indent=4))
    print(report['results'][0]['place_id'])
