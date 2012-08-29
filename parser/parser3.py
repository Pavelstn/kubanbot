# -*- coding: utf-8 -*-
import urllib
# подключили библиотеку urllib
import lxml.html
from lxml.html import fromstring
url = 'http://forums.kuban.ru/f1274/'
content = urllib.urlopen(url).read()
doc = fromstring(content)
doc.make_links_absolute(url)

print lxml.html.tostring(doc)

