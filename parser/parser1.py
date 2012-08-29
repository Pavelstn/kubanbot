# -*- coding: utf-8 -*-


import lxml.html
# подключили библиотеку

doc = lxml.html.document_fromstring("""<html>
 <body>
   <span class="simple_text">One</span> text</br>
   <span class="cyrillic_text">Второй</span> текст</br>
 </body>
</html>
""")
# Получили HTML-документ со строки

txt1 = doc.xpath('/html/body/span[@class="simple_text"]/text()[1]')
# Находим тег «span», у которого аттрибут «class» равен значению «simple_text» и с помощью функции text() получаем текст элемента
txt2 = doc.xpath('/html/body/span[@class="cyrillic_text"]/following-sibling::text()[1]')
# Находим тег «span», у которого аттрибут «class» равен значению «cyrillic_text» и получаем следующий за ним текст с помощью following-sibling (получаем следующий в ветке элемент) и text()
# Для получение значений использовался XPath
print  txt1
print txt2