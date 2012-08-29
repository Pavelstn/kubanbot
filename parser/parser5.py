# -*- coding: utf-8 -*-

import lxml
import lxml.html
from lxml import etree


html= etree.Element("html")
body= etree.SubElement(html,"body")
body.text= "TEXT"

br= etree.SubElement(body, "br")
br.tail="AAAA"
print (etree.tostring(html))

print(html.xpath("string()"))
print(html.xpath("//text()"))

build_text_lists= etree.XPath("//text()")
print(build_text_lists(html))

texts= build_text_lists(html)
print(texts[0])

parent= texts[0].getparent()
print(parent.tag)

print(texts[1])
print(texts[1].getparent().tag)

root= etree.Element("root")
etree.SubElement(root,"child").text= "Child 1"
etree.SubElement(root,"child").text= "Chold 2"
etree.SubElement(root,"another").text= "Child 3"

print(etree.tostring(root, pretty_print=True))

for element in root.iter("*"):
	print("%s- %s"%(element.tag, element.text))

