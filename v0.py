# -*- coding: utf-8 -*-

import http.client
import re
import urllib.parse
import urllib.request

def getSendsmsPage(conn):
#Получает страничку www.ycc.ru/sendsms/
    conn.request('GET', '/sendsms/')
    return conn.getresponse().read().decode('cp1251')

def getCaptchaInfo(conn):
#'''Ищет в странице отправки смс ссылку на каптчу и возвращает информацию из неё'''
    sendsmsPage = getSendsmsPage(conn)
    captchaSrc = re.search(r'/i/sms/sms\.php\?s=([0-9]{8})', sendsmsPage)
    return {'path': captchaSrc.group(0), 'magic': captchaSrc.group(1)}

def downloadCaptcha(conn, captchaAddress):
#'''Скачивает каптчу по адресу captchaAddress в файл captcha.png'''
    conn.request('GET', captchaAddress)
    f = open('captcha.png', 'wb')
    f.write(conn.getresponse().read())
    f.close()

def getCaptcha(conn):
#'''Скачивает каптчу в файл captcha.png и возвращает её magic number, которое передаётся в запросе под именем cc'''
    captchaInfo = getCaptchaInfo(conn)
    print('Captcha address: ' + captchaInfo['path'])
    downloadCaptcha(conn, captchaInfo['path'])

    return captchaInfo['magic']

def sendSms():
    conn = http.client.HTTPConnection('www.ycc.ru')

    #Разбираемся с капчей
    #cc - число в адресе каптчи, нужно для отправки POST-запроса
    cc = getCaptcha(conn)
    captchaCode = int(input('Code: '))

    #Параметры POST-запроса
    params = urllib.parse.urlencode({'from_name': 'Имя', 'prefix': 790892, 'phone_number': 12345,
                                'text_sms': '123', 'imgcc': captchaCode, 'cc': cc, 'sendsms': 'yes', 'submit.x': 52, 'submit.y': 11,
                                'sim': 257})

    #Заголовки
    headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.7) Gecko/20100106 Ubuntu/9.10 (karmic) Firefox/3.5.7'}

    #Отправка POST-запроса для отсылки смс
    conn.request('POST', '/sendsms/', params, headers)
    #Печать ответа сервера
    print(conn.getresponse().read().decode('cp1251'))

    conn.close()

sendSms()