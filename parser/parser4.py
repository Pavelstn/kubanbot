import urllib2

from lxml import etree


URL = 'http://forums.kuban.ru/f1274/'

html = urllib2.urlopen(URL).read()
tree = etree.fromstring(html, parser=etree.HTMLParser())

tree.xpath('//script')
# [<Element script at 102f831b0>,
#  ...
#  <Element script at 102f83ba8>]

tree.xpath('//style')
# [<Element style at 102f83c58>]

tags_to_strip = ['script', 'style']
etree.strip_elements(tree, *tags_to_strip)

tree.xpath('//style')
# []

tree.xpath('//script')
# []

body = tree.xpath('//body')
body = body[0]

text = ' '.join(body.itertext())
tokens = text.split()
# [u'Stack',
#  u'Exchange',
#  u'log',
#  u'in',
#  ...
#  u'Stack',
#  u'Overflow',
#  u'works',
#  u'best',
#  u'with',
#  u'JavaScript',
#  u'enabled']

print tokens