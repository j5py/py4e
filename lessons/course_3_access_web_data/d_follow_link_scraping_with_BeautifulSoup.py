
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


test = ssl.create_default_context()
test.check_hostname = False
test.verify_mode = ssl.CERT_NONE


def get_href_from(location, position):
    data = urllib.request.urlopen(location, context=test).read()
    soup = BeautifulSoup(data, 'html.parser')
    anchor = soup('a')[position -1]
    return (anchor.contents[0], anchor.get('href', None))


url = 'http://py4e-data.dr-chuck.net/known_by_Nuala.html'

child = 18 # Find the link at position 18 (first is 1, not 0)
count = 0 # Follow that link, repeat this process 7 times
name = None # The answer is the last name that you retrieve


while count < 7:
    print(name, url)
    crawled = get_href_from(url, child)
    name = crawled[0]
    url = crawled[1]
    count += 1

print(name) # The first character of the name of the last page that you will load is: A
