# -*- coding: utf-8 -*-

import urllib.parse, urllib.request, http.cookiejar
import re

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.7) Gecko/20100106 Ubuntu/9.10 (karmic) Firefox/3.5.7'),
('Referer', 'http://ycc.ru/sendsms/'), ('Accept-Charset', 'utf-8')]

#получение странички ycc.ru/sendsms/
page = opener.open('http://ycc.ru/sendsms/').read().decode('cp1251')

#работа с капчей
captchaSrc = re.search(r'/i/sms/sms\.php\?s=([0-9]{8})', page)
urllib.request.urlretrieve('http://www.ycc.ru' + captchaSrc.group(0), 'captcha.png')
c = int(input('Code: '))
cc = captchaSrc.group(1)

#параметры POST-запроса
params = urllib.parse.urlencode({'from_name': 'NAME', 'prefix': 790892, 'phone_number': 12345, 'text_sms': 'Hello, world!', 'imgcc': c, 'cc': cc})
#POST-запрос на отправку смс
page = opener.open('http://ycc.ru/sendsms/', params).read().decode('cp1251')
print(page)