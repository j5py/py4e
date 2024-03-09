
import urllib.request
import xml.etree.ElementTree as ET
import ssl


test = ssl.create_default_context()
test.check_hostname = False
test.verify_mode = ssl.CERT_NONE


url = 'https://py4e-data.dr-chuck.net/comments_1778123.xml'


# Extract the comment counts from the XML data, compute the sum of the numbers in the file

handle = urllib.request.urlopen(url, context=test)

data = handle.read()
tree = ET.fromstring(data)
tags = tree.findall('.//count')

total = 0


for tag in tags:
    total += int(tag.text)

print(total)
