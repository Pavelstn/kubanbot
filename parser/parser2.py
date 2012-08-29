# -*- coding: utf-8 -*-
import urllib
# подключили библиотеку urllib
import lxml.html
from lxml import etree
# подключили библиотеку lxml

page = urllib.urlopen("http://forums.kuban.ru/f1274/")
# Открываем наш любимый Хабр

doc = lxml.html.document_fromstring(page.read())
#doc= page.read()
#txt1 = doc.xpath('//*[@id="thread_title_2960973"][1]')
#print txt1


#print lxml.html.tostring(doc)
#for topic in doc.cssselect('font-weight:bold'):
#    print topic.text
#for topic in doc.xpath('//*[@id="thread_title_2777734"]')
 #   print topic.text


#find = doc.xpath("//b")
#print(find(doc)[0].tag)

#idd= doc.get_element_by_id("threadbits_forum_1274")
#print lxml.html.tostring(idd)

##lxml.html.fromstring(page).text_content()
idd= doc.text_content()
print lxml.html.tostring(idd)