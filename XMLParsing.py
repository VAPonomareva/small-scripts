import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

summa = 0
xtm = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_934714.xml').read()
tree = ET.fromstring(xtm)
counts = tree.findall('.//count')
for item in counts:
    summa += int(item.text)
print(summa)