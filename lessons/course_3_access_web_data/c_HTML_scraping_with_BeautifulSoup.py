
# CLI: pip3 install beautifulsoup4

from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl


# Ignore SSL certificate errors

test = ssl.create_default_context()
test.check_hostname = False
test.verify_mode = ssl.CERT_NONE


# Parse the data, extract numbers and calculate sum of numbers in file

sample_url = 'http://py4e-data.dr-chuck.net/comments_42.html'
student_url = 'http://py4e-data.dr-chuck.net/comments_1778121.html'

data = urlopen(student_url, context=test).read()
soup = BeautifulSoup(data, 'html.parser')
tags = soup('span')
count = 0

for tag in tags:
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Attrs:', tag.attrs)
    count += int(tag.contents[0])

print(count)
