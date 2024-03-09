
import urllib.request
import json
import ssl


test = ssl.create_default_context()
test.check_hostname = False
test.verify_mode = ssl.CERT_NONE


url = 'https://py4e-data.dr-chuck.net/comments_1778124.json'


# Extract the comment counts from the JSON data, compute the sum of the numbers in the file

handle = urllib.request.urlopen(url, context=test)

data = handle.read()
report = json.loads(data)
comments = report['comments']

total = 0


for key in comments:
    total += key['count']

print(total)
